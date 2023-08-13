from fastapi import FastAPI
from app.routes.v1 import activities
from app.routes.v2 import activities_v2


app = FastAPI()

app.include_router(activities.router)
app.include_router(activities_v2.router)
