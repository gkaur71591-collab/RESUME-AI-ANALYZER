from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.database import base
from sqlalchemy import String,DateTime,ForeignKey,Text
from datetime import datetime

class Resume(base):
    __tablename__="resumes"

    id:Mapped[int]=mapped_column(
        primary_key=True,
        index=True
    )

    user_id:Mapped[int]=mapped_column(
        ForeignKey("users.id"),
        nullable=False    
    )

    file_name:Mapped[str]=mapped_column(
        String(500),
        nullable=False
    )
    file_path: Mapped[str] = mapped_column(
    String(500),
    nullable=False
)

    file_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    extracted_text: Mapped[str | None] = mapped_column(
    Text,
    nullable=True
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="uploaded",
        nullable=False
    )
    analysis_status: Mapped[str] = mapped_column(
    String(50),
    default="uploaded",
    nullable=False,
    index=True
)
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    user = relationship(
        "User",
        back_populates="resumes"
    )
    analysis_started_at:Mapped[datetime | None] = mapped_column(
    DateTime, 
    nullable=True
    )
    analysis_completed_at: Mapped[datetime | None] = mapped_column(
    DateTime,
    nullable=True
    )
    analysis = relationship(
    "ResumeAnalysis",
    back_populates="resume",
    uselist=False
    )  
     
    job_matches = relationship(
    "JobMatch",
    back_populates="resume",
    cascade="all, delete-orphan"
    )