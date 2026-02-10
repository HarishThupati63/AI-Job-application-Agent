from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Job Application Agent"
    database_url: str = "postgresql+psycopg://user:password@localhost:5432/job_agent"
    redis_url: str = "redis://localhost:6379/0"


settings = Settings()
