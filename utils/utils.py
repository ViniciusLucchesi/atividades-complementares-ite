import re
import json


def match_regex(observation:str)-> tuple:
    """
    Encontra e devolve em formato de tuplas o número do grupo e a quantidade de horas
    que serão contabilizadas com a atividade atual.

    Caso essa informação não seja encontrada será retornada uma tupla com zeros (0,0)
    """
    match = re.search(r"[0-9]{1}: [0-9]{1,2}", observation)
    if match:
        resp_group, resp_hours = match.group().split(':')
        hours = int(re.search(r"[0-9]{1,}", resp_hours).group())
        group = int(re.search(r"[0-9]{1,}", resp_group).group())
        return (hours, group)
    return (0, 0)

def return_location_and_online(location:str) -> tuple[str, bool]:
    match = re.search(r"(zoom)", location.lower())
    if match:
        return (location, True)
    return (location, False)


def sort_activities(data:list, reverse:bool) -> list:
    """
    Retorna a lista ordenada de maneira crescente ou decrescente por quantidades de horas oferecidas
    """
    print(reverse)
    return sorted(data, key=lambda obj: obj['hours'], reverse=reverse)

def valid_response(status_code:int) -> bool:
    if status_code == 200:
        return True
    return False
 
# def success_json(activities:list, order_by:dict) -> json:
#     sorted_activitie = sort_activities(activities, order_by)
#     return json.dumps(sorted_activitie, indent=4, ensure_ascii=False)

# def error_json(status_code:int) -> json:
#     error = {"erro": "A página não foi encontrada", "status_code":status_code}
#     return json.dumps(error, ensure_ascii=False)
