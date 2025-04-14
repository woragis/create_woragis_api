import os

import redis

from core.config import settings

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT, db=0, decode_responses=True)
