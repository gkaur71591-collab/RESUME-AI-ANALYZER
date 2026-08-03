from app.worker.celery import celery_app

from app.database.database import SessionLocal

from app.models.user import User
from app.models.resume import Resume
from app.models.resume_analysis import ResumeAnalysis
from app.models.job_match import JobMatch
from datetime import datetime
from app.services.rag_service import (
    create_resume_vector_store,
    get_resume_retriever
)

from app.services.ai_service import analyze_with_rag

import json
from app.core.logger import logger


@celery_app.task(
    bind=True,
    max_retries=3
)
def analyze_resume_task(self, resume_id: int):

    db = SessionLocal()

    try:

        resume = db.query(Resume).filter(
            Resume.id == resume_id
        ).first()


        if not resume:
            return "Resume not found"

        logger.info(f"Starting analysis for Resume ID: {resume_id}")
        # Update status when task starts
        resume.analysis_status = "processing"
        resume.analysis_started_at = datetime.utcnow()
        db.commit()


        # Create vector store

        create_resume_vector_store(
            resume.extracted_text,
            resume.id
        )

        logger.info(f"Vector store created for Resume ID: {resume_id}")
        # Get retriever

        retriever = get_resume_retriever(
            resume.id
        )


        # Retrieve relevant chunks

        docs = retriever.invoke(
            "Analyze skills, experience, education and missing skills"
        )


        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )


        # AI analysis
        logger.info(f"Sending Resume ID {resume_id} to Ollama")
        ai_response = analyze_with_rag(
            context
        )


        analysis_json = json.loads(
            ai_response
        )


        # Save analysis

        analysis = ResumeAnalysis(
            resume_id=resume.id,
            analysis_result=analysis_json
        )


        db.add(analysis)


        # Update completed status

        resume.analysis_status = "completed"
        resume.analysis_completed_at = datetime.utcnow()

        db.commit()

        logger.info(f"Analysis completed successfully for Resume ID: {resume_id}")
        return {
            "resume_id": resume_id,
            "status": "completed"
        }


    except Exception as e:
        logger.exception(f"Analysis failed for Resume ID: {resume_id}")
        db.rollback()

    try:

        raise self.retry(
            exc=e,
            countdown=60
        )


    except self.MaxRetriesExceededError:
        resume = db.query(Resume).filter(
            Resume.id == resume_id
        ).first()


        if resume:

            resume.analysis_status = "failed"

            db.commit()


        return {
            "status": "failed",
            "error": str(e)
        }


    finally:

        db.close()