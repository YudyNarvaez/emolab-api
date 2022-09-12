import datetime
from dataclasses import dataclass, field
from typing import List
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base, mapper_registry, now

@mapper_registry.mapped
@dataclass
class User(Base):

    __tablename__ = "user"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(
        init=False,
        metadata={"sa": Column(Integer, primary_key=True)},
    )

    email: str = field(
        metadata={"sa": Column(String(254), nullable=False, unique=True, index=True)}
    )

    hashed_password: str = field(metadata={"sa": Column(String(128), nullable=False)})

    name: str = field(
        metadata={"sa": Column(String(50), nullable=False)}
    )

    last_name: str = field(
        default=None,
        metadata={"sa": Column(String(50), nullable=True)}
    )

    nit: str = field(
        default=None,
        metadata={"sa": Column(String(20), nullable=True)}
    )

    address: str = field(
        default=None,
        metadata={"sa": Column(String(50), nullable=True)}
    )

    contact: str = field(
        default=None,
        metadata={"sa": Column(String(50), nullable=True)}
    )

    is_parent: bool = field(
        default=True,
        metadata={"sa": Column(Boolean(), nullable=False)}
    )

    is_health_professional: bool = field(
        default=False,
        metadata={"sa": Column(Boolean(), nullable=False)}
    )

    kids: List['Kid'] = field(
        init=False,
        default_factory=list,
        metadata={"sa": relationship("Kid", lazy="selectin")}
    )

    created_at: datetime.datetime = field(
        default=datetime.datetime.now(tz=datetime.timezone.utc),
        metadata={"sa": Column(DateTime(timezone=True), nullable=False)},
    )

    updated_at: datetime.datetime = field(
        default=None,
        metadata={"sa": Column(DateTime(timezone=True), onupdate=now, nullable=True)},
    )

    __mapper_args__ = {"eager_defaults": True}  # type: ignore