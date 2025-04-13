import redis
import os

from config.index import settings

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT, db=0, decode_responses=True)
