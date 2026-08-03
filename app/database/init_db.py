from app.database import base, engine

from app.models.user import User
from app.models.resume import Resume
from app.models.resume_analysis import ResumeAnalysis
from app.models.job_match import JobMatch

base.metadata.create_all(bind=engine)