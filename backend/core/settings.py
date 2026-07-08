from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Powered Multi-Agent Learning Assistant"
    APP_VERSION: str = "1.0.0"

    LLM_PROVIDER: str
    GROQ_API_KEY: str
    MODEL_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()