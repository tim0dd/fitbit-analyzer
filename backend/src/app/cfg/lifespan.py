from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    #TODO ingest data
    yield
    #TODO close connections, clean up etc
    print("Shutting down...")

