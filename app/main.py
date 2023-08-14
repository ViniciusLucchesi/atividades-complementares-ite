from fastapi import FastAPI
from app.routes import activities


app = FastAPI()

app.include_router(activities.router)
