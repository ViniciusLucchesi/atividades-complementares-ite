from typing import Annotated
from fastapi import APIRouter, Depends
from app.scraping.student_area import ScraperInscriptions
from app.database.surrealdb import SurrealDB
from fastapi.security import HTTPBasic, HTTPBasicCredentials



router = APIRouter(
    prefix='/api/v2',
    tags=['v2']
)

security = HTTPBasic()


@router.get('/subscriptions')
async def get_subscriptions(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    payload = {
        "matricula": credentials.dict()['username'],
        "password": credentials.dict()['password']
    }
    scraper = ScraperInscriptions(payload)
    database = await SurrealDB.get_activites()
    return {'scraper': scraper.activities(), 'database': database}