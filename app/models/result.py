import datetime
from dataclasses import dataclass, field
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base, mapper_registry, now

@mapper_registry.mapped
@dataclass
class Result(Base):

    __tablename__ = "result"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(
        init=False,
        metadata={"sa": Column(Integer, primary_key=True)},
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