from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Text
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.database import base
from sqlalchemy.dialects.postgresql import JSONB


class ResumeAnalysis(base):

    __tablename__ = "resume_analysis"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )


    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id"),
        nullable=False
    )

    analysis_result: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    resume = relationship(
        "Resume",
        back_populates="analysis"
    )