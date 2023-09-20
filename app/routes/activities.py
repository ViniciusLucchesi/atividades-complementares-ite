from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from app.scraping import activities, auth_activities


router = APIRouter(
    prefix='/api/v2',
    tags=['v2']
)

security = HTTPBasic()



@router.get('/activities')
async def get_activities(group: int = None):
    if group is not None:
        if group not in range(1, 5):
            return [{'error': 'O parâmetro (group) deve ser de 1 á 4'}]
    
    data = activities.get_activities(group)
    if len(data) == 0:
        return [{'error': f'Não há atividades para o grupo {group}'}]
    return data


@router.get('/activities/registrations')
async def get_activity_link(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    payload = {
        "matricula": credentials.dict()['username'],
        "password": credentials.dict()['password']
    }
    return auth_activities.get_activities_link(payload)
