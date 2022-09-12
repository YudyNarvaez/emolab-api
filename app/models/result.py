import datetime
from dataclasses import dataclass, field
from typing import Any, Dict
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, JSON
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

    kid_id: int = field(
        metadata={"sa": Column(Integer, ForeignKey("kid.id"), nullable=False)},
    )

    text: str = field(
        metadata={"sa": Column(String(150), nullable=False)}
    )

    analysis: Dict[str, Any] = field(
        default=None, metadata={"sa": Column(JSON, nullable=False)}
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