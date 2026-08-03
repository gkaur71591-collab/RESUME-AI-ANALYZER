from pydantic import BaseModel
from datetime import datetime
##ResumeResponse – Returned after uploading a resume
class ResumeResponse(BaseModel):
    id:int
    file_name:str
    file_type:str
    extracted_text: str | None
    status:str
    uploaded_at:datetime

    model_config={
        "from_attributes":True
    }
##ResumeListResponse – Returned when listing all resumes
class ResumeListResponse(BaseModel):
    id: int
    file_name: str
    status: str | None
    uploaded_at: datetime

    model_config={
            "from_attributes":True
    }
