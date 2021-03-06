import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".local_env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Boldd API"
    PROJECT_VERSION: str = "1.0.0"

    # add hooks to pull database connection properties
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 120  # in mins


settings = Settings()
