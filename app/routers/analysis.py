from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from app.database.database import get_db

from app.models.resume import Resume
from app.models.resume_analysis import ResumeAnalysis
from app.models.job_match import JobMatch

from app.schemas import resume
from app.schemas.job_match import JobMatchRequest
from app.core.rate_limit import limiter
from app.auth.dependencies import current_user
from fastapi import Request
from app.services.rag_service import (
    create_resume_vector_store,
    get_resume_retriever
)

from app.services.ai_service import (
    analyze_with_rag,
    analyze_job_match
)

from app.worker.tasks import analyze_resume_task
router = APIRouter(
    prefix="/analysis",
    tags=["AI Analysis"]
)
from app.core.logger import logger

# ===============================
# Generate Resume Analysis
# ===============================

@router.post("/{resume_id}")
@limiter.limit("5/minute")
def analyze_resume_file(
    request:Request,
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(current_user)
):

    # Check resume exists and add onwership check
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()


    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )
    logger.info(
    f"User {current_user.id} started analysis for Resume {resume.id}"
    )
## new code ##
    resume.analysis_status = "processing"

    db.commit()

    db.refresh(resume)

    # Send background job to Celery
    analyze_resume_task.delay(
        resume_id
    )
    logger.info(
    f"Celery task queued for Resume {resume.id}"
    )

    return {
        "resume_id": resume_id,
        "message": "Resume analysis started",
        "status": "processing"
    }

# ===============================
# Job Match
# ===============================

@router.post("/{resume_id}/job-match")
@limiter.limit("5/minute")
def job_match(
    resume_id: int,
    request: Request,
    job_request: JobMatchRequest,
    db: Session = Depends(get_db),
    current_user=Depends(current_user)
):


    # Get resume

    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()

    logger.info(
    f"Job match requested for Resume {resume.id}"
)
    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )



    # Create vector store

    create_resume_vector_store(
        resume.extracted_text,
        resume.id
    )



    # Retriever

    retriever = get_resume_retriever(
        resume.id
    )



    docs = retriever.invoke(
        job_request.job_description
    )



    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )



    # AI job matching

    ai_response = analyze_job_match(
        context,
        job_request.job_description
    )



    # Save job match

    job_match = JobMatch(

        resume_id=resume.id,

        job_description=job_request.job_description,

        match_result=ai_response

    )



    db.add(job_match)

    db.commit()

    db.refresh(job_match)
    logger.info(
    f"Job match completed for Resume {resume.id}"
    )


    return {

        "resume_id": resume.id,

        "job_match_id": job_match.id,

        "match_result": job_match.match_result

    }


# ===============================
# Get Analysis Status
# ===============================

@router.get("/status/{resume_id}")
def get_analysis_status(
    resume_id: int,
    db: Session = Depends(get_db)
):

    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()


    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    logger.info(
    f"Analysis fetched for Resume {resume_id}"
    )
    return {

        "resume_id": resume.id,

        "status": resume.analysis_status,
         "started_at": resume.analysis_started_at, 
        
        "completed_at": resume.analysis_completed_at

    }
# ===============================
# Get Resume Analysis
# ===============================

@router.get("/{resume_id}")
def get_analysis(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(current_user)
):


    analysis = db.query(
        ResumeAnalysis
    ).join(
        Resume
    ).filter(
        ResumeAnalysis.resume_id == resume_id,
        Resume.user_id == current_user.id
    ).order_by(
        ResumeAnalysis.id.desc()
    ).first()



    if not analysis:

        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    logger.info(
    f"Status requested for Resume {resume.id}: {resume.analysis_status}"
    )

    return {

        "resume_id": resume_id,

        "analysis_id": analysis.id,

        "analysis": analysis.analysis_result,

       
        

    }