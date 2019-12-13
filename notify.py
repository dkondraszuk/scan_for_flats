from flats import all_flats
import web_scrapper as ws
from urllib.parse import urljoin

BASE_URL = 'https://www.archicom.pl/m/'


def compare_price_and_status(flat):
    html = ws.get_html(urljoin(BASE_URL, flat.id))
    status = ws.get_flat_status(html)
    price = ws.get_flat_price(html)
    if status != flat.status:
        notify_about_status_change()
    if price != flat.price:
        notify_about_price_change()
    update_flat()


def notify_about_status_change():
    pass


def notify_about_price_change():
    pass


def update_flat():
    pass


if __name__ == '__main__':
    for flat in all_flats:
        compare_price_and_status(flat)
