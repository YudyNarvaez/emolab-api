"""SQLAlchemy async engine and sessions tools"""

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker

from app.core import config

sqlalchemy_database_uri = config.settings.SQLALCHEMY_DATABASE_URI


async_engine = create_async_engine(
    sqlalchemy_database_uri, pool_pre_ping=True, future=True
)
async_session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)  # type: ignore

if TYPE_CHECKING:
    async_session: sessionmaker[AsyncSession]  # type: ignore
