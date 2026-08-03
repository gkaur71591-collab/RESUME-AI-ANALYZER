from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REDIS_URL: str
    OPENAI_MODEL: str = "gpt-4.1-mini"
    OPENAI_API_KEY: str
    GEMINI_API_KEY: str
    OLLAMA_HOST: str
    class Config:
        env_file=".env.dev",
        case_sensitive = True

settings = Settings()
