import ollama
import json
from app.core.config import settings
def get_ollama_client():
    return ollama.Client(
         host=settings.OLLAMA_HOST
    )

def analyze_with_rag(context: str):

    prompt = f"""
You are an ATS resume analyzer.

Analyze the resume context below.

Return ONLY valid JSON.
Do not add markdown.
Do not add explanations.

Calculate ATS score based on:

- Technical skills match (40%)
- Experience relevance (25%)
- Projects (15%)
- Education (10%)
- Keywords and resume completeness (10%)

Important:
- ats_score must always be a number between 0 and 100.
- Do not return null.
- Do not return 0 unless the resume has no useful information.
JSON format:

{{
    "skills": [],
    "experience_years": "",
    "education": {{
        "degree": "",
        "field_of_study": "",
        "institution": "",
        "graduation_date": ""
    }},
    "summary": "",
    "ats_score": 75,
    "missing_skills": [],
    "improvement_suggestions": []
}}

Resume Context:

{context}
"""

    client = get_ollama_client()
    response = client.chat(
        model="llama3.1",
        format="json",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    ai_result = response["message"]["content"]


    # validate JSON response
    try:
        json.loads(ai_result)
    except json.JSONDecodeError:
        return {
            "error": "Invalid AI response format",
            "raw_response": ai_result
        }


    return ai_result

#####
def analyze_job_match(
    resume_context: str,
    job_description: str
):

    prompt = f"""
You are an expert ATS and technical recruiter.

Compare the resume with the job description.

Return ONLY valid JSON.

JSON format:

{{
    "match_score": 75,
    "matched_skills": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "recommendations": []
}}

Resume:

{resume_context}

Job Description:

{job_description}
"""

    client = get_ollama_client()
    response = client.chat(
        model="llama3.1",
        format="json",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response["message"]["content"]

    # Convert JSON string -> Python dict
    ai_result = json.loads(result)

    return ai_result