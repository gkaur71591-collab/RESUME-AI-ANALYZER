# 🚀 AI Resume Analyzer

A production-ready **AI Resume Analyzer** built with **FastAPI**, **Ollama Local LLM**, **LangChain**, **RAG (Retrieval Augmented Generation)**, **PostgreSQL**, **Redis**, **Celery**, and **Docker**.

The application allows users to securely upload resumes, analyze resume quality, compare resumes with job descriptions, identify skill gaps, and generate AI-powered recommendations.

The project follows modern backend engineering practices including authentication, authorization, testing, logging, exception handling, rate limiting, containerization, CI automation, and environment-based configuration.

---

# ✨ Features

## Authentication & Security

* User Registration
* User Login
* JWT Authentication
* OAuth2 Password Flow
* Authorization & Protected APIs
* Argon2 Password Hashing
* Role-Based Access Control
* API Rate Limiting
* Secure Environment Configuration

---

## AI Resume Analysis

* Resume Upload
* Resume Text Extraction
* AI Resume Evaluation
* Job Description Matching
* Skill Gap Analysis
* Resume Improvement Suggestions
* AI Recommendations

---

## RAG (Retrieval Augmented Generation)

The application uses RAG architecture to provide context-aware AI responses.

Features:

* Document Loading
* Text Chunking
* Embedding Generation
* Vector Search
* Context Retrieval
* AI Response Generation

RAG Components:

* LangChain
* Chroma Vector Database
* Ollama Local LLM

---

# 🧠 AI Architecture

```text
              Resume Upload
                    |
                    |
            Document Processing
                    |
                    |
             Text Chunking
                    |
                    |
              Embeddings
                    |
                    |
          Chroma Vector Database
                    |
                    |
          Similarity Search
                    |
                    |
        Retrieved Context + Query
                    |
                    |
              Ollama LLM
                    |
                    |
          AI Resume Analysis
```

---

# 🛠 Technology Stack

## Backend

* Python 3.11
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic

## Database

* PostgreSQL

## Authentication

* JWT
* OAuth2
* Argon2

## AI / LLM

* Ollama
* LangChain
* ChromaDB
* RAG Pipeline

## Background Processing

* Celery
* Redis

## DevOps

* Docker
* Docker Compose
* GitHub Actions
* Render

## Testing

* pytest
* FastAPI TestClient

---

# 🏗 System Architecture

```text
                     Client
                       |
                       |
                 FastAPI API
                       |
        +--------------+--------------+
        |              |              |
 Authentication   Resume API     Health API
        |
        |
   Service Layer
        |
+-------+---------+-------------+
|                 |             |
PostgreSQL      Redis        Ollama
|                 |
Database       Celery Worker
                  |
             Background Jobs
```

---

# 📁 Project Structure

```text
AI-RESUME-ANALYZER

├── app
│   ├── api
│   ├── auth
│   ├── core
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   ├── database
│   ├── middleware
│   ├── models
│   ├── routers
│   ├── schemas
│   ├── services
│   ├── tasks
│   ├── utils
│   └── main.py
│
├── tests
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_health.py
│   └── test_users.py
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.development
├── .env.production
└── README.md
```

---

# ⚙️ Environment Configuration

The application supports separate development and production environments.

## Development Environment

File:

```text
.env.development
```

Used for:

* Local PostgreSQL
* Local Redis
* Local Ollama
* Debug logging
* Development secrets

---

## Production Environment

File:

```text
.env.production
```

Used for:

* Cloud database
* Managed Redis
* Production secrets
* Optimized logging
* Production configurations

---

# 🔐 Environment Variables

Example:

```env
DATABASE_URL=postgresql://username:password@host:5432/database

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30


REDIS_URL=redis://localhost:6379


OLLAMA_BASE_URL=http://localhost:11434

OLLAMA_MODEL=llama3.1
```

---

# 🤖 Ollama Setup

Install Ollama:

https://ollama.com/download

Check installation:

```bash
ollama --version
```

Pull model:

```bash
ollama pull llama3.1
```

Run Ollama:

```bash
ollama serve
```

Default API:

```text
http://localhost:11434
```

---

# 🚀 Run Application Locally

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-RESUME-ANALYZER.git
```

Go inside project:

```bash
cd AI-RESUME-ANALYZER
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

Swagger:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 🐳 Docker Setup

Build image:

```bash
docker build -t resume-analyzer .
```

Run container:

```bash
docker run -p 8000:8000 resume-analyzer
```

Using Docker Compose:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

# ❤️ Health Check

Endpoint:

```http
GET /health
```

Example:

```json
{
 "status":"healthy",
 "database":"connected",
 "redis":"connected",
 "ollama":"connected"
}
```

Docker Compose also includes container health checks.

---

# ⚡ Celery Background Processing

Celery handles long-running tasks.

Used for:

* Resume processing
* AI analysis
* Report generation
* Email notifications

Architecture:

```text
FastAPI
   |
   |
Redis Broker
   |
   |
Celery Worker
   |
   |
Background Task
```

---

# 🛡 Error Handling & Logging

## Global Exception Handling

Implemented custom exception handlers for:

* HTTP Exceptions
* Validation Errors
* Database Errors
* Internal Server Errors

Benefits:

* Consistent API responses
* Better debugging
* Improved reliability

---

## Logging

Centralized logging captures:

* Application events
* API requests
* Exceptions
* Background tasks
* Startup/shutdown events

---

# 🚦 API Rate Limiting

Rate limiting protects APIs from:

* Abuse
* Excessive requests
* Brute-force attacks

Implemented for sensitive endpoints:

* Login
* Registration
* AI processing APIs

---

# 🧪 Testing

Testing framework:

* pytest
* FastAPI TestClient

Covered:

* User Registration
* Login
* JWT Token Creation
* Invalid Credentials
* Protected Routes
* Health API

Run tests:

```bash
pytest
```

Verbose:

```bash
pytest -v
```

Coverage:

```bash
pytest --cov=app
```

---

# 🔄 GitHub Actions CI

CI workflow:

```text
.github/workflows/ci.yml
```

Pipeline:

* Checkout Code
* Setup Python
* Install Dependencies
* Run Tests
* Validate Application

Triggered on:

* Push
* Pull Requests

---

# ☁️ Deployment

The application is Dockerized and ready for cloud deployment.

Supported platforms:

* Render
* AWS
* Azure
* Railway
* Google Cloud

Production deployment requires:

* Database URL
* Redis URL
* Environment variables
* Ollama hosted separately or cloud LLM provider

---

# 🔮 Future Enhancements

* ATS Resume Score
* Interview Question Generator
* AI Career Assistant
* Resume Version Management
* Admin Dashboard
* Analytics Dashboard
* Email Notifications
* Kubernetes Deployment

---

# 🤝 Contribution

1. Fork repository

2. Create branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add feature"
```

4. Push changes

```bash
git push origin feature/new-feature
```

5. Create Pull Request

---

# 👩‍💻 Author

**Gagandeep Kaur**

Senior Backend Engineer | AI Engineering

Skills:

* Python
* FastAPI
* PostgreSQL
* Redis
* Celery
* Docker
* JWT
* LangChain
* Ollama
* RAG
* CI/CD
* REST APIs

GitHub:

https://github.com/YOUR_USERNAME

LinkedIn:

https://linkedin.com/in/YOUR_PROFILE

---

# 📄 License

MIT License
