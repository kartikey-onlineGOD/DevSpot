import requests
from bs4 import BeautifulSoup
import web_scraper as wsb
from urllib.parse import quote

def search_devpost(keywords):
    encoded_keywords = quote(keywords)
    search_url = f'https://devpost.com/software/search?query={encoded_keywords}'
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        software_list = data.get('software', [])
        urls = [entry['url'] for entry in software_list if 'url' in entry]
        return urls
    else:
        return None
    



