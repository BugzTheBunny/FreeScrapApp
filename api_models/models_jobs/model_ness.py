import requests


def format_job(opportunity):
    return {'title': opportunity['Title'],
            'company': 'Ness',
            'url': f'https://www.ness-tech.co.il/careers/job/{opportunity["Index"]}',
            'date': f'Job ID : {opportunity["Index"]}',
            'description': None,
            'location': opportunity['PosLocation'],
            'source': 'www.ness-tech.co.il/'
            }


def get_ness_jobs(keyword):
    jobs_list = requests.get(
        f'https://nesshr.ness-tech.co.il/api/services/GetOrderDetailsList?freeText={keyword}').json()
    clean_jobs_list = []
    for job in jobs_list['AllOrderDetailsList']:
        clean_jobs_list.append(format_job(job))
    return clean_jobs_list
