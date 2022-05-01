from fastapi import FastAPI

from routers import random, deterministic

app = FastAPI(root_path="/api)

app.include_router(random.router)
app.include_router(deterministic.router)
