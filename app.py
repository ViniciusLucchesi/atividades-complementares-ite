# Library Importations
import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import json
import re


# Defining Models
@dataclass
class Activities:
    date: dict
    event: str
    professor: str
    observation: str
    location: str

@dataclass
class Response:
    body_html: HTMLParser
    status_code: int


# Functions
def get_page(client, url) -> Response:
    headers = {"User-Agent": "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"}
    resp = client.get(url, headers=headers)
    html = HTMLParser(resp.text)
    return Response(body_html=html, status_code=resp.status_code)

def parse_activities(html) -> list:
    table = html.css_first("table#dtBasicExample > tbody")
    
    headers = ['date', 'theme', 'event', 'professor', 'observation', 'time', 'location']    
    pattern = r"Grupo [0-9]{1}: [0-9]{1,2}h"

    data = []
    for row in table.css('tr'):        
        row_data = [cell.text().strip() for cell in row.css('td')]
        row_dict = dict(zip(headers, row_data))

        match = re.search(pattern, row_dict['observation'])
        if match:            
            group, hours = match.group().split(':')
            row_dict['hours'] = re.search(r"[0-9]{1,}", hours).group()
            row_dict['group'] = re.search(r"[0-9]{1,}", group).group()
        
        
        data.append(row_dict)
    return data
    

def main():
    client = httpx.Client()
    url = "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"
    
    page = get_page(client, url)
    if page.status_code == 200:
        activities = parse_activities(page.body_html)
        json_data = json.dumps(activities, indent=4, ensure_ascii=False)
    else:
        error = {"Erro": "A página não foi encontrada", "code":page.status_code}
        json_data = json.dumps(error, ensure_ascii=False)
    
    print(json_data)

if __name__ == '__main__':
    main()
