from fastapi import APIRouter
from app.scraping.v2 import pandas


router = APIRouter(
    prefix='/api/v2',
    tags=['v2']
)



@router.get('/activities')
async def activities(group: int = None):
    if group is not None:
        if group not in range(1, 5):
            return {'error': 'group must be in range 1-4'}
    
    data = pandas.get_activities(group)
    if len(data) == 0:
        return {'error': f'Não há dados para o grupo {group}'}
    return data
