from fastapi import Request, HTTPException
from utils.redis_client import r
from typing import Callable


def get_rate_limiter(rate_limit: int, time_window: int) -> Callable:
    def rate_limiter(request: Request):
        ip = request.client.host
        path = request.url.path
        key = f"ratelimit:{ip}:{path}"

        current = r.get(key)
        if current is None:
            r.set(key, 1, ex=time_window)
        else:
            current = int(current)
            if current >= rate_limit:
                ttl = r.ttl(key)
                raise HTTPException(
                    status_code=429,
                    detail=f"Rate limit exceeded: {rate_limit}/{time_window}s. Try again in {ttl}s.",
                )
            else:
                r.incr(key)
    return rate_limiter
