from fastapi import FastAPI
from .api.health import router as health_router
from .api.upload import router as upload_router

app=FastAPI()
app.include_router(health_router)
app.include_router(upload_router)
