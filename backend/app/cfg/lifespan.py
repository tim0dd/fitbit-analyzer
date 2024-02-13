from contextlib import asynccontextmanager

from fastapi import FastAPI

import app.cfg.fitbit_access as fitbit_access


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    fitbit_access_token_available = fitbit_access.try_find_fitbit_access_token()
    if fitbit_access_token_available:
        #TODO: enable fitbit api background tasks
        pass
    yield
    #TODO: close connections, clean up etc
    print("Shutting down...")
