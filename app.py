# Library Importations
import httpx
import json
import re
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print


@dataclass
class Response:
    body_html: HTMLParser
    status_code: int


def get_page(client, url) -> Response:
    headers = {"User-Agent": "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"}
    resp = client.get(url, headers=headers)
    html = HTMLParser(resp.text)
    return Response(body_html=html, status_code=resp.status_code)

def match_regex(observation):
    match = re.search(r"[0-9]{1}: [0-9]{1,2}", observation)
    if match:
        resp_group, resp_hours = match.group().split(':')
        hours = int(re.search(r"[0-9]{1,}", resp_hours).group())
        group = int(re.search(r"[0-9]{1,}", resp_group).group())
        return hours, group
    return 0, 0

def parse_activities(html) -> list:
    table = html.css_first("table#dtBasicExample > tbody")        

    # [   0   ,   1    ,   2   ,      3     ,       4      ,   5   ,     6     ]
    # ['date', 'theme', 'event', 'professor', 'observation', 'hour', 'location']
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
