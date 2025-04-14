import os

from dotenv import load_dotenv
from pydantic import BaseSettings

# Load .env file
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Woragis API"
    API_VERSION: str = "v1"

    # Database
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URL: str = (
        f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    # JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET", "super-secret")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}"

    # Rate limiting
    RATE_LIMIT_PREFIX: str = "rl:"
    RATE_LIMIT_DEFAULT: int = 100  # fallback


settings = Settings()
