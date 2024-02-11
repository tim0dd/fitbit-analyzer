import logging
from fastapi import APIRouter, FastAPI
from app.routers import sleep
from app.cfg.lifespan import lifespan
from app.cfg.log import LoggingRoute
from app.cfg.cors import cors_config

app = FastAPI(lifespan=lifespan)
app.add_middleware(**cors_config)
router = APIRouter(route_class=LoggingRoute)
logging.basicConfig(filename='info.log', level=logging.DEBUG)
app.include_router(sleep.router, prefix="/api/v1/sleep", tags=["Sleep"])
# app.include_router(other_module.router)
