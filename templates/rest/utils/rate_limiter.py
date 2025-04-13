import time
from fastapi import Request, HTTPException
from typing import Callable

# Dictionary: IP → List[timestamps]
VISITS = {}


def get_rate_limiter(rate_limit: int, time_window: int) -> Callable:
    def rate_limiter(request: Request):
        ip = request.client.host
        now = time.time()
        window_visits = VISITS.setdefault(ip, {})

        key = f"{request.url.path}:{rate_limit}:{time_window}"
        timestamps = window_visits.setdefault(key, [])

        # Remove old timestamps
        timestamps = [t for t in timestamps if now - t < time_window]
        window_visits[key] = timestamps

        if len(timestamps) >= rate_limit:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded: {rate_limit} per {time_window} seconds"
            )

        timestamps.append(now)
    return rate_limiter
