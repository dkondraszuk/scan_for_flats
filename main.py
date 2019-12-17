from urllib.parse import urljoin

import web_scrapper as ws
import db_session
import notify

BASE_URL = 'https://www.archicom.pl/m/'


if __name__ == '__main__':
    all_flats = db_session.select_all_flats()
    for flat in all_flats:
        html = ws.get_html(url=urljoin(BASE_URL, flat.flat_id))
        new_status = ws.get_flat_status(html)
        new_price = ws.get_flat_price(html)
        if new_status != flat.status and new_price != flat.price:
            notify.send_sms_about_change()  # todo: with status and price params
            db_session.update_flat(flat_floor=flat.floor, new_status=new_status, new_price=new_price)
        elif new_status != flat.status:
            notify.send_sms_about_change()  # todo: with status param only
            db_session.update_flat(flat_floor=flat.floor, new_status=new_status)
        elif new_price != flat.price:
            notify.send_sms_about_change()  # todo: with price param only
            db_session.update_flat(flat_floor=flat.floor, new_price=new_price)

    updated_flats = db_session.select_all_flats()  # todo: remove
    for up_flat in updated_flats:
        print(up_flat)
