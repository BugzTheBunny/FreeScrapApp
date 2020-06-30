import requests
from bs4 import BeautifulSoup
from app_properties import headers


data = BeautifulSoup(requests.get('https://freecoursesite.com/?s=', headers=headers).text,'lxml')
print(data.find('div','listing listing-grid listing-grid-1 clearfix columns-2'))
