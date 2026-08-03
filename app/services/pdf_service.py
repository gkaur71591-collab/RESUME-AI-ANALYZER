### This keeps your routers focused on handling HTTP requests, while services handle the actual work.

import fitz


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    document = fitz.open(file_path)

    for page in document:
        text += page.get_text()

    document.close()

    return text