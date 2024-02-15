from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

import app.cfg.fitbit_access as fitbit_access
from app.services.fitbit_sync_service import FitbitSyncService
from app.cfg.logging import LOGGING_CONFIG


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("Starting up...")
    fitbit_access_token_available = fitbit_access.try_find_fitbit_access_token()
    if fitbit_access_token_available:
        fitbit_sync_service = FitbitSyncService()
        await fitbit_sync_service.start_sync()
    yield
    # TODO: close connections, clean up etc
    print("Shutting down...")
