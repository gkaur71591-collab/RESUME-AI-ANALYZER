from datetime import datetime

from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    id: int
    resume_id: int
    analysis_result: dict
    created_at: datetime
    model_config = {
        "from_attributes": True
    }