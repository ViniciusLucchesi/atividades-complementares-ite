import re


def return_hours_and_group(observation:str)-> tuple[int, int]:
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
    """
    Encontra e devolve em formato de tuplas a localização coletada via Scraping e a um
    boleano que indica se será uma atividade no formato online ou não.
    """
    match = re.search(r"(zoom)", location.lower())
    if match:
        return (location, True)
    return (location, False)


def format_professor_name(name:str) -> str:
    match = re.search(r"(\/)", name)
    if match:
        return name.upper()
    return name.title()


def sort_activities(data:list, reverse:bool) -> list:
    """
    Retorna a lista ordenada de maneira crescente ou decrescente por quantidades de horas oferecidas
    """
    return sorted(data, key=lambda obj: obj['hours'], reverse=reverse)
