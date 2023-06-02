from dataclasses import dataclass
from selectolax.parser import HTMLParser
import httpx

from utils import match_regex


@dataclass
class Response:
    body_html: HTMLParser
    status_code: int


@dataclass
class Scraper:
    url = "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"
    headers = {"User-Agent": "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"}

    def get_page(self, client:httpx.Client) -> Response:
        """
        Retorna a classe "Response", contendo o HTML da página buscada 
        e o status da página para controle de erros.
        """        
        resp = client.get(self.url, headers=self.headers)
        html = HTMLParser(resp.text)
        return Response(body_html=html, status_code=resp.status_code)

    def parse_activities(self, html:HTMLParser) -> list:
        """
        Retorna uma lista de objetos JSON contendo todos os itens 
        encontrados durante o web scraping.
        """
        table = html.css_first("table#dtBasicExample > tbody")
        data = []
        for row in table.css('tr'):
            row_data = [cell.text().strip() for cell in row.css('td')]
            hours, group = match_regex(row_data[4])
            data_dict = {
                "date": " ".join([row_data[0], row_data[5]]),
                "event": row_data[2],
                "professor": row_data[3],
                "observation": row_data[4],
                "location": row_data[6],
                "hours": hours,
                "group": group
            }
            data.append(data_dict)
        return data