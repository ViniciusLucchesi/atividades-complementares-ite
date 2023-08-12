from fastapi import APIRouter
from app.scraping.v1 import tools
from app.models.enums import Sorted


router = APIRouter(
    prefix='/api/v1',
    tags=['v1']
)



@router.get('/activities')
async def activities(group: int|None=None, sorted: Sorted|None=None):
    if sorted:
        if sorted is Sorted.asc:
            return tools.return_data(group, False)
        elif sorted is Sorted.desc:
            return tools.return_data(group, True)
    
    return tools.return_data(group)
