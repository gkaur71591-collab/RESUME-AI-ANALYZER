from pathlib import Path

from fastapi import HTTPException, status

from app.services.pdf_service import extract_text_from_pdf
from app.services.docx_service import extract_text_from_docx


def extract_resume_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Unsupported file format."
    )