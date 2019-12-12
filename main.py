import requests
from bs4 import BeautifulSoup
from contextlib import closing
from urllib.parse import urljoin

BASE_URL = 'https://www.archicom.pl/m/'

flats = {
    1: urljoin(BASE_URL, '13902'),
    2: urljoin(BASE_URL, '13941'),
    3: urljoin(BASE_URL, '13931'),
    4: urljoin(BASE_URL, '14023'),
    5: urljoin(BASE_URL, '14005'),
    6: urljoin(BASE_URL, '14011'),
    7: urljoin(BASE_URL, '13968'),
}


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
    for floor, flat in flats.items():
        print(f'{floor}: {is_flat_available(flat)}')
