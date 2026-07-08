from fastapi import FastAPI
from backend.api.routes import router
from backend.core.settings import settings
from backend.core.logger import logger

logger.info("Starting AI Powered Multi-Agent Learning Assistant...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Multi-Agent AI Learning Assistant"
)

app.include_router(router)