import logging
from contextlib import closing

import requests
from bs4 import BeautifulSoup

from my_logger import log


def get_request(url):
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_resp(resp):
                return resp.content
    except requests.RequestException as e:
        log(logging.ERROR, f'Error during request to {url} : {e}')


def is_good_resp(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and 'html' in content_type)


def get_html(url):
    raw_html = get_request(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    return html


def get_flat_status(html):
    td_status = html.find('td', class_='status')
    raw_status = td_status.text
    clean_status = raw_status.strip()[8:]  # cut leading 'Status: ' string
    return clean_status


def get_flat_price(html):
    input_price = html.find('script')
    raw_price = input_price.text
    price_index = raw_price.find('price')
    price = raw_price[price_index + 8: price_index + 8 + 6]  # +8 to cut leading string, +6 due to 6 digit price
    return int(price)
