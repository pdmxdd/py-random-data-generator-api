from fastapi import FastAPI

from routers import random, deterministic

app = FastAPI(
    openapi_url = "/api/openapi.json",
    docs_url = "/api/docs",
    redoc_url = "/api/redoc"
)

app.include_router(random.router)
app.include_router(deterministic.router)
