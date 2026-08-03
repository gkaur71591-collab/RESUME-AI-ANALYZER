from pathlib import Path
from uuid import uuid4
from fastapi import APIRouter,Depends,File,UploadFile,HTTPException,status
from app.database.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.schemas.resume import ResumeResponse
from app.auth.dependencies import current_user
from app.services.resume_service import extract_resume_text
from app.schemas.resume import ResumeListResponse

from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)

UPLOAD_DIR=Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
ALLOWED_EXTENSIONS = {".pdf", ".docx"}
@router.post(
    "/upload",
    response_model=ResumeResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(current_user),
    db: Session = Depends(get_db),
):
    extension = Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details="only pdf and docs are allowed",
        )
    unique_filename = f"{uuid4()}{extension}"
    file_path = UPLOAD_DIR / unique_filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_resume_text(
    str(file_path)
    )


    resume = Resume(
    user_id=current_user.id,
    file_name=file.filename,
    file_path=str(file_path),
    file_type=extension.replace(".", ""),
    extracted_text=extracted_text,
    status="extracted",
    analysis_status="uploaded"
    )  
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume
@router.get("/",response_model=list[ResumeListResponse])
def get_my_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(current_user)
):

    resumes = db.query(Resume).filter(
        Resume.user_id == current_user.id
    ).all()


    return resumes
