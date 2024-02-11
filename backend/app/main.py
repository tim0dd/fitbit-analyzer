from contextlib import asynccontextmanager
import logging
from fastapi import APIRouter, FastAPI
from app.routers import sleep
from app.cfg.lifespan import lifespan
from app.cfg.log import LoggingRoute


app = FastAPI(lifespan=lifespan)
router = APIRouter(route_class=LoggingRoute)
logging.basicConfig(filename='info.log', level=logging.DEBUG)
app.include_router(sleep.router, prefix="/api/v1/sleep", tags=["Sleep"])
# app.include_router(other_module.router)
