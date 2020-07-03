# Udemy API Module.
# API Overview = https://www.udemy.com/developers/affiliate/
import os
import requests

auth_token = os.environ.get('AUTH_TOKEN')
headers = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": f"{auth_token}",
    "Content-Type": "application/json;charset=utf-8"
}


def request_udemy_api(query):
    try:
        return requests.get(
            f'https://www.udemy.com/api-2.0/courses/?page_size={100}&search={query}'
            f'&price=price-free&language=en&ratings=4', headers=headers).json()['results']
    except:
        return False


def clean_data(data):
    clean_data = []
    for each in data:
        clean_data.append({
            'title': str(each['title']),
            "url": f"https://www.udemy.com{each['url']}",
            'description': each['headline'],
            'image': each['image_480x270'],
            'source': 'Udemy'
        })
    return clean_data


def get_udemy_courses(query):
    clean_json = clean_data(request_udemy_api(query))
    return clean_json


