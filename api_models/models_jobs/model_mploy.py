import json
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=utf-8",
    'pragma': 'no-cache',
    'referer': 'https',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36',
}

def format_job(opportunity):
    return {'title': opportunity['title'],
            'company': opportunity['companyid'],
            'url': f'https://www.mploy.co.il/job/details/{opportunity["jobid"]}',
            'date': opportunity['updated_at'][0:10],
            'description': opportunity['description'],
            'location': opportunity['formatted_address'],
            'source': 'www.mploy.co.il'
            }


def get_mploy_jobs(keyword, limit):
    page = 0
    jobs_list = []
    keep_running = True
    while keep_running:
        call = requests.get(
            f'https://www.mploy.co.il/jobs?distance=1000&orderby=updatedAt&direction=DESC&'
            f'start={page}&type=LOCATION&'
            f'keyword={keyword}', headers=headers)
        json_response = json.loads(call.content)
        if len(json_response['jobs']) == 0 or page > limit:
            return jobs_list
        else:
            for opportunity in json_response['jobs']:
                jobs_list.append(format_job(opportunity))
        page = page + 10