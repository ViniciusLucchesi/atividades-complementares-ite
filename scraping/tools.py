from httpx import Client
from .model_scraper import Scraper
from utils.utils import valid_response, sort_activities


def return_data(filter:int|None=None, sorted:bool|None=None) -> dict[str, str|int|bool]:
    client = Client()
    scraper = Scraper()
    response = scraper.get_page(client)
    if valid_response(response.status_code):
        activities = scraper.parse_activities(response.body_html, filter)
        if sorted != None:
            return sort_activities(activities, sorted)
        return activities
    return {'error': f'Something get wrong where we try to extract the HTML page from ({scraper.url})'}
