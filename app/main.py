from fastapi import FastAPI
from app.routes import activities
from app.routes import subscriptions
from app.database.surrealdb import SurrealDB


app = FastAPI(
    title="ITE Activities API",
    version="2.0.5"
)


@app.on_event('startup')
async def startup():
    await SurrealDB.connect()

@app.on_event('shutdown')
async def shutdown():
    await SurrealDB.close()



app.include_router(activities.router)
app.include_router(subscriptions.router)
