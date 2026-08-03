from datetime import datetime

from pydantic import BaseModel


class JobMatchRequest(BaseModel):

    job_description: str


class JobMatchResponse(BaseModel):

    id: int

    resume_id: int

    job_description: str

    match_result: dict

    created_at: datetime


    model_config = {
        "from_attributes": True
    }