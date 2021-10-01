from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .routers import api_router

api = FastAPI()
api.include_router(api_router)
Instrumentator().instrument(api).expose(api, include_in_schema=False, should_gzip=True)