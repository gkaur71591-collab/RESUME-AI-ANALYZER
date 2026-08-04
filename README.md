# 🚀 AI Resume Analyzer

A production-ready **AI Resume Analyzer** built with **FastAPI**, **Ollama Local LLM**, **LangChain**, **RAG (Retrieval Augmented Generation)**, **PostgreSQL**, **Redis**, **Celery**, and **Docker**.

The application allows users to securely upload resumes, analyze resume quality, compare resumes with job descriptions, identify skill gaps, and generate AI-powered recommendations.

The project follows modern backend engineering practices including authentication, authorization, testing, logging, exception handling, rate limiting, containerization, CI/CD automation, and environment-based configuration.

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

# 🧠 RAG (Retrieval Augmented Generation)

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
* GitHub Container Registry
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
├── Dockerfile.prod
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

OLLAMA_HOST=http://localhost:11434

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
git clone https://github.com/gkaur71591-collab/RESUME-AI-ANALYZER.git
```

Go inside project:

```bash
cd RESUME-AI-ANALYZER
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

Install dependencies:

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

# 🐳 Docker Setup

The application is fully containerized using Docker.

## Build Docker Image

```bash
docker build -t resume-analyzer .
```

## Run Docker Container

```bash
docker run -p 8000:8000 resume-analyzer
```

## Run With Docker Compose

```bash
docker compose up --build
```

## Stop Containers

```bash
docker compose down
```

Docker Compose manages:

* FastAPI application
* PostgreSQL database
* Redis
* Celery worker
* Supporting services

---

# ❤️ Health Check

Health endpoint:

```http
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "database": "connected",
  "redis": "connected",
  "ollama": "connected"
}
```

Health checks validate:

* Application availability
* Database connectivity
* Redis connectivity
* Ollama availability

Docker Compose also includes service health checks.

---

# ⚡ Celery Background Processing

Celery is used for asynchronous background processing.

Used for:

* Resume processing
* AI analysis
* Report generation
* Long-running tasks

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
 Background Tasks
```

Benefits:

* Faster API responses
* Better scalability
* Handles resource-intensive operations asynchronously

---

# 🛡 Error Handling & Logging

## Global Exception Handling

Custom exception handlers are implemented for:

* HTTP Exceptions
* Validation Errors
* Database Exceptions
* Internal Server Errors

Benefits:

* Consistent API responses
* Better debugging
* Improved reliability
* Centralized error management

---

## Application Logging

Centralized logging captures:

* Application events
* API requests
* Exceptions
* Background tasks
* Startup/shutdown events

Logging helps with:

* Debugging
* Monitoring
* Production troubleshooting

---

# 🚦 API Rate Limiting

Rate limiting protects APIs from:

* Abuse
* Excessive requests
* Brute-force attacks

Implemented for sensitive endpoints:

* Authentication APIs
* Registration APIs
* AI processing APIs

Benefits:

* Improved security
* Better resource management
* Protection against malicious requests

---

# 🧪 Testing

The project includes automated tests using:

* pytest
* FastAPI TestClient

## Test Coverage

Covered scenarios:

* User Registration
* User Login
* JWT Token Generation
* Invalid Credentials
* Protected Routes
* Health API

Run tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Generate coverage:

```bash
pytest --cov=app
```

---

# 🔄 CI/CD Pipeline

The project implements a complete automated CI/CD pipeline using **GitHub Actions**.

The pipeline automates testing, Docker image creation, security scanning, and deployment.

## CI/CD Workflow

```text
Developer
    |
    |
Git Push / Pull Request
    |
    |
GitHub Actions
    |
    |
PostgreSQL Test Container
    |
    |
Database Connection Validation
    |
    |
Alembic Migration Testing
    |
    |
Pytest Automation
    |
    |
Docker Image Build
    |
    |
Push Image to GitHub Container Registry
(GHCR)
    |
    |
Docker Security Scan
(Trivy)
    |
    |
Render Deployment Trigger
    |
    |
Production Environment
```

---

# Continuous Integration (CI)

The CI pipeline performs:

* Repository checkout
* Python 3.11 setup
* Dependency installation
* PostgreSQL 16 test database startup
* Database connection validation
* Alembic migration validation
* Automated unit testing

Technologies:

* GitHub Actions
* PostgreSQL Service Container
* pytest
* Alembic

---

# Continuous Deployment (CD)

The deployment pipeline performs:

* Production Docker image build
* Docker image publishing to GHCR
* Vulnerability scanning using Trivy
* Automated Render deployment

Technologies:

* Docker Buildx
* GitHub Container Registry
* Trivy Security Scanner
* Render Deploy Hooks

---

# GitHub Actions Workflow

Location:

```text
.github/

└── workflows/

    └── ci.yml
```

Pipeline triggers:

* Push to main branch
* Push to master branch
* Pull requests

---

# ☁️ Deployment

The application is Dockerized and ready for cloud deployment.

Supported platforms:

* Render
* AWS
* Azure
* Railway
* Google Cloud Platform

Production deployment requires:

* PostgreSQL database URL
* Redis connection URL
* Environment variables
* Secret keys
* Ollama hosted separately or managed LLM provider

Deployment process:

```text
GitHub Repository
        |
        |
GitHub Actions
        |
        |
Docker Image
        |
        |
GitHub Container Registry
        |
        |
Render Deployment
        |
        |
Production API
```

---

# 🔐 Production Considerations

Implemented production practices:

* Environment-based configuration
* JWT authentication
* Secure password hashing
* API rate limiting
* Database migrations
* Health monitoring
* Containerization
* Automated testing
* CI/CD automation

---

# 🤝 Contribution

1. Fork the repository

2. Create a feature branch:

```bash
git checkout -b feature/new-feature
```

3. Commit changes:

```bash
git commit -m "Add new feature"
```

4. Push changes:

```bash
git push origin feature/new-feature
```

5. Create a Pull Request

---

# 👩‍💻 Author

**Gagandeep Kaur**

Senior Backend Engineer | AI Engineering

## Skills

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Redis
* Celery
* Docker
* JWT Authentication
* LangChain
* Ollama
* RAG
* REST APIs
* CI/CD
* Cloud Deployment

GitHub:

```text
https://github.com/gkaur71591-collab
```

LinkedIn:

```text
https://linkedin.com/in/YOUR_PROFILE
```

---

# 📄 License

MIT License

http://localhost:8000/redoc
```
