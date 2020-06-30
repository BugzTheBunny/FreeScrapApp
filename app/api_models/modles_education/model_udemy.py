# Udemy API Module.
# API Overview = https://www.udemy.com/developers/affiliate/

import requests
from ..api_properties import AUTH_TOKEN
from app_properties import udemy_data_size
auth_token = AUTH_TOKEN

headers = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": f"{auth_token}",
    "Content-Type": "application/json;charset=utf-8"
}


def request_udemy_api(query):
    try:
        return requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size={udemy_data_size}&search={query}'
            f'&price=price-free&language=en&ratings=4.5', headers=headers).json()['results']
    except:
        return False


def clean_data(data):
    clean_data = []
    for each in data:
        clean_data.append({
            'title': str(each['title']),
            "url": f"udemy.com{each['url']}",
            'headline': each['headline']
        })
    return clean_data


def get_udemy_courses(query):
    clean_json = clean_data(request_udemy_api(query))
    return clean_json

