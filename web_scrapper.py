from contextlib import closing
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import flats


BASE_URL = 'https://www.archicom.pl/m/'


def get_request(url):
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_resp(resp):
                return resp.content
    except requests.RequestException as e:
        print(f'Error during request to {url} : {e}')


def is_good_resp(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and 'html' in content_type)


def is_flat_available(url):
    raw_html = get_request(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    flat_status = html.find_all('td', class_='status')
    for item in flat_status:
        if 'wolny' in item.text:
            return True
    return False


if __name__ == '__main__':
    for flat in flats.all_flats:
        print(f'Floor {flat.floor}: {is_flat_available(urljoin(BASE_URL, flat.id))}')
