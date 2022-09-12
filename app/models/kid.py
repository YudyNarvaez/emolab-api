import datetime
from dataclasses import dataclass, field
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, mapper_registry, now

@mapper_registry.mapped
@dataclass
class Kid(Base):

    __tablename__ = "kid"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(
        init=False,
        metadata={"sa": Column(Integer, primary_key=True)},
    )

    user_id: int = field(
        metadata={"sa": Column(Integer, ForeignKey("user.id"), nullable=True)},
    )

    name: str = field(metadata={"sa": Column(String(50), nullable=False)})

    last_name: str = field(metadata={"sa": Column(String(50), nullable=False)})

    birthday: datetime.date = field(
        metadata={"sa": Column(Date, nullable=False)},
    )

    has_asperger: bool = field(
        default=False,
        metadata={"sa": Column(Boolean(), nullable=False)}
    )

    gender: str = field(
        default= 'M',
        metadata={"sa": Column(String(1), nullable=False)}
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