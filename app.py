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


# Scraping functions
def get_page(client, url) -> Response:
    """
    Retorna a classe "Response", contendo o HTML da página buscada 
    e o status da página para controle de erros.
    """
    headers = {"User-Agent": "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"}
    resp = client.get(url, headers=headers)
    html = HTMLParser(resp.text)
    return Response(body_html=html, status_code=resp.status_code)

def parse_activities(html) -> list:
    """
    É uma função responsável por montar uma lista de JSONs com os dados
    coletados via scraping.

    ---
    O que é retornado na variável "row_data":
    \t['date', 'theme', 'event', 'professor', 'observation', 'hour', 'location']\n
    \t[   0   ,   1    ,   2   ,      3     ,       4      ,   5   ,     6     ]

    ---
    Retorna uma lista com vários dicionários
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


# Util functions
def match_regex(observation)-> tuple:
    """
    Encontra e devolve em formato de tuplas o número do grupo e a quantidade de horas
    que serão contabilizadas com a atividade atual.
    """
    match = re.search(r"[0-9]{1}: [0-9]{1,2}", observation)
    if match:
        resp_group, resp_hours = match.group().split(':')
        hours = int(re.search(r"[0-9]{1,}", resp_hours).group())
        group = int(re.search(r"[0-9]{1,}", resp_group).group())
        return (hours, group)
    return (0, 0)

def sort_activities(activities: list, order_by_data: dict) -> list:
    element, reverse = order_by_data.values()
    return sorted(activities, key=lambda obj: obj[element], reverse=reverse)

def valid_response(page: Response) -> bool:
    if page.status_code == 200:
        return True
    return False

def error_json(page: Response) -> json:
    error = {"Erro": "A página não foi encontrada", "code":page.status_code}
    return json.dumps(error, ensure_ascii=False)
    
def success_json(activities: list, order_by: dict) -> json:
    sorted_activitie = sort_activities(activities, order_by)
    return json.dumps(sorted_activitie, indent=4, ensure_ascii=False)


# Main function
def main():
    client = httpx.Client()
    url = "https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis"
    
    page = get_page(client, url)
    if valid_response(page):
        order = {'element': 'hours', 'reverse': False}
        activities = parse_activities(page.body_html)
        json_data = success_json(activities=activities, order_by=order)
    else:
        json_data = error_json(page)
    print(json_data)


if __name__ == '__main__':
    main()
