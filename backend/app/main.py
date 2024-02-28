from fastapi import APIRouter, FastAPI
from app.routers import sleep
from app.cfg.lifespan import lifespan
from app.cfg.logged_route import LoggedRoute
from app.cfg.cors import cors_config
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, **cors_config)
router = APIRouter(route_class=LoggedRoute)
app.include_router(sleep.router, prefix="/api/v1/sleep", tags=["Sleep"])
