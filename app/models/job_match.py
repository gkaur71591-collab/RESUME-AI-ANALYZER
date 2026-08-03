from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Text
)

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.database import base


class JobMatch(base):

    __tablename__ = "job_match"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )


    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id"),
        nullable=False
    )


    job_description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


    match_result: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    resume = relationship(
        "Resume",
        back_populates="job_matches"
    )