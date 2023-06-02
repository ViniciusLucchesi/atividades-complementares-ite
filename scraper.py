from httpx import Client
from models import Scraper
from utils import valid_response, success_json, error_json


def main():
    client = Client()
    scraper = Scraper()
    page = scraper.get_page(client)

    if valid_response(page.status_code):
        activities = scraper.parse_activities(page.body_html)
        json_data = success_json(activities=activities, order_by=scraper.order)
    else:
        json_data = error_json(page.status_code)
    print(json_data)



if __name__ == '__main__':
    main()
