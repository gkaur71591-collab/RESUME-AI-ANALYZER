from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.auth.router import router as auth_router
from app.routers.users import router as users_router
from app.routers.resumes import router as resumes_router
from app.routers.analysis import router as analysis_router
from app.core.rate_limit import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health
from app.core.config import settings

print(
    f"Running environment: {settings.APP_ENV}"
)
@asynccontextmanager
async def lifespan(app: FastAPI):


    yield
app = FastAPI(
    title="AI Resume Analyzer",
    lifespan=lifespan
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    health.router
)
app.include_router(
    auth_router
)
app.include_router(
    users_router
)

app.include_router(
    resumes_router
)
app.include_router(
    analysis_router
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API running"
    }
