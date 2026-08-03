from fastapi import APIRouter
from sqlalchemy import text
import redis
import ollama

from app.database.database import engine

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def health_check():

    health = {
        "status": "healthy",
        "database": "unknown",
        "redis": "unknown",
        "ollama": "unknown"
    }


    # Check PostgreSQL
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        health["database"] = "connected"

    except Exception as e:
        health["database"] = "failed"



    # Check Redis
    try:

        redis_client = redis.Redis(
            host="redis",
            port=6379,
            db=0
        )

        redis_client.ping()

        health["redis"] = "connected"

    except Exception:
        health["redis"] = "failed"



    # Check Ollama

    try:

        client = ollama.Client(
            host="http://host.docker.internal:11434"
        )

        client.list()

        health["ollama"] = "running"

    except Exception:
        health["ollama"] = "failed"



    return health