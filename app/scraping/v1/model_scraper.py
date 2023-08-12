from httpx import Client
from dataclasses import dataclass
from pydantic import BaseModel
from selectolax.parser import HTMLParser
from app.utils.v1 import utils

@dataclass
class Response():
    body_html: HTMLParser
    status_code: int

    def is_valid(self) -> bool:
        if self.status_code == 200:
            return True
        return False


class Scraper(BaseModel):
    url: str = 'https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis'
    headers: dict[str, str] = {'User-Agent': 'https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis'}

    def get_page(self, client: Client) -> Response:
        response = client.get(self.url, headers=self.headers)
        html = HTMLParser(response.text)
        return Response(body_html=html, status_code=response.status_code)
    
    def parse_activities(self, html: HTMLParser, filter:int|None=None) -> list[dict[str, str|int|bool]]:
        # Se o filtro for menor que 1 ou maior que 4, retorna erro  
        if filter is not None:      
            if filter < 1 or filter > 4:
                return [{"error": f"O grupo {filter} não existe"}]

        table = html.css_first('table#dtBasicExample > tbody')
        data = []
        for row in table.css('tr'):
            row_data = [cell.text().strip() for cell in row.css('td')]
            hours, group = utils.return_hours_and_group(row_data[4])
            location, online = utils.return_location_and_online(row_data[6])
            professor = utils.format_professor_name(row_data[3])

            if filter is not None:
                if group == filter:
                    data_dict = {
                        "date": " ".join([row_data[0], row_data[5]]),
                        "event": row_data[2],
                        "professor": professor,
                        "observation": row_data[4],
                        "location": location,
                        "online": online,
                        "hours": hours,
                        "group": group
                    }
                    data.append(data_dict)
            else:
                data_dict = {
                    "date": " ".join([row_data[0], row_data[5]]),
                    "event": row_data[2],
                    "professor": professor,
                    "observation": row_data[4],
                    "location": location,
                    "online": online,
                    "hours": hours,
                    "group": group
                }
                data.append(data_dict)
        
        if len(data) == 0:
            data = [{"error": f"Não há atividades para o grupo {filter}"}]
        return data    
