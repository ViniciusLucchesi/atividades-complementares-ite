from enum import Enum
from scraping import tools
from fastapi import FastAPI


class Sorted(str, Enum):
    asc = 'asc'
    desc = 'desc'

app = FastAPI()


@app.get('/api/activities')
async def activities(group: int|None=None, sorted: Sorted|None=None):
    if sorted:
        if sorted == Sorted.asc:
            return tools.return_data(group, False)
        elif sorted == Sorted.desc:
            return tools.return_data(group, True)
    
    return tools.return_data(group)
