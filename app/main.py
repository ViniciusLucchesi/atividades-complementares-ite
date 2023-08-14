from fastapi import FastAPI
from app.routes import activities


app = FastAPI(
    title="ITE Activities API",
    version="2.0.5"
)

app.include_router(activities.router)
