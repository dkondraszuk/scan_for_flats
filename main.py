# from flats_info import all_flats
import web_scrapper as ws
from urllib.parse import urljoin
from db_session import select_all_flats, update_flat

BASE_URL = 'https://www.archicom.pl/m/'


def compare_price_and_status(flat):
    # html = ws.get_html(urljoin(BASE_URL, flat.id))
    # status = ws.get_flat_status(html)
    # price = ws.get_flat_price(html)
    # if status != flat.status:
    #     notify_about_status_change()
    # if price != flat.price:
    #     notify_about_price_change()
    # update_flat()
    pass


def notify_about_change():
    pass


if __name__ == '__main__':
    all_flats = select_all_flats()
    for flat in all_flats:
        html = ws.get_html(url=urljoin(BASE_URL, flat.flat_id))
        new_status = ws.get_flat_status(html)
        new_price = ws.get_flat_price(html)
        if new_status != flat.status and new_price != flat.price:
            notify_about_change()  # todo: with status and price params
            update_flat(flat_floor=flat.floor, new_status=new_status, new_price=new_price)
        elif new_status != flat.status:
            notify_about_change()  # todo: with status param only
            update_flat(flat_floor=flat.floor, new_status=new_status)
        elif new_price != flat.price:
            notify_about_change()  # todo: with price param only
            update_flat(flat_floor=flat.floor, new_price=new_price)

    updated_flats = select_all_flats()
    for up_flat in updated_flats:
        print(up_flat)
