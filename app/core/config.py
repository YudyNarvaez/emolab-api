"""
File with environment variables and general configuration logic.
`SECRET_KEY`, `ENVIRONMENT` etc. map to env variables with the same names.

Pydantic priority ordering:

1. (Most important, will overwrite everything) - environment variables
2. `.env` file in root folder of project
3. Default values

For project name, version, description we use pyproject.toml
For the rest, we use file `.env` (gitignored), see `.env.example`

`SQLALCHEMY_DATABASE_URI`:
Both are ment to be validated at the runtime, do not change unless you know
what are you doing. All the two validators do is to build full URI (TCP protocol)
to databases to avoid typo bugs.

See https://pydantic-docs.helpmanual.io/usage/settings/

Note, complex types like lists are read as json-encoded strings.
"""
from typing import Dict, List, Literal

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, PostgresDsn, validator


class Settings(BaseSettings):
    # CORE SETTINGS
    API_V1_STR: str = "/api/v1"
    ROOT_PATH: str = ""
    SECRET_KEY: str
    ENVIRONMENT: Literal["DEV", "PYTEST", "STG", "PRD"] = "DEV"
    SECURITY_BCRYPT_ROUNDS: int = 12
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 40320  # 28 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    # POSTGRESQL DEFAULT DATABASE
    DATABASE_HOSTNAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    DATABASE_DB: str
    SQLALCHEMY_DATABASE_URI: str = ""

    # FIRST SUPERUSERd
    FIRST_SUPERUSER_FULL_NAME: str
    FIRST_SUPERUSER_ROLE: str
    FIRST_SUPERUSER_EMAIL: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    

    @validator("SQLALCHEMY_DATABASE_URI")
    def _assemble_db_connection(cls, v: str, values: Dict[str, str]) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["DATABASE_USER"],
            password=values["DATABASE_PASSWORD"],
            host=values["DATABASE_HOSTNAME"],
            port=values["DATABASE_PORT"],
            path=f"/{values['DATABASE_DB']}",
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings: Settings = Settings()  # type: ignore
