import os
from dotenv import load_dotenv
from typing import Optional
from surrealdb import Surreal

load_dotenv()
DB = Surreal("ws://surrealdb:8000/rpc")


class SurrealDB(Surreal):
    def __init__(self, url: Optional[str] = None, token: Optional[str] = None) -> None:
        super().__init__(url, token)

    async def connect() -> None:
        try:
            await DB.connect()
            await DB.signin({'user': os.getenv('DB_USER'), 'pass': os.getenv('DB_PASS')})
            await DB.use(namespace='ITE', database='Atividades')
        except Exception as error:
            print(f"ERROR: {error}")
    
    async def get_activites():
        try:
            data = await DB.select('activities')
            return data
        except Exception as error:
            return {
                'message': 'Error when executing "SurrealDB.get_activites()"',
                'error': str(error)
            }
    
    async def set_activitie(id: str, protocol: str):
        try:
            await DB.query('CREATE type::thing($tb, $id) SET activitie = $id, protocol = $protocol', {'tb': 'activities', 'id': id, 'protocol': protocol})
        except Exception as error:
            return {
                'message': 'Error when executing "SurrealDB.set_activitie()"',
                'error': str(error)
            }
    