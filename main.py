import datetime
import logging
from urllib.parse import urljoin

import db_session
import notify
import web_scrapper as ws
from my_logger import log

BASE_URL = 'https://www.archicom.pl/m/'


if __name__ == '__main__':
    exec_time = datetime.datetime.now()
    str_exec_time = exec_time.strftime('%d.%m.%Y %H:%M')
    log(logging.INFO, '*** New scan session started! Date: {} ***'.format(str_exec_time))
    all_flats = db_session.select_all_flats()
    for flat in all_flats:
        html = ws.get_html(url=urljoin(BASE_URL, flat.flat_id))
        new_status = ws.get_flat_status(html)
        new_price = ws.get_flat_price(html)
        if new_status != flat.status and new_price != flat.price:
            db_session.update_flat(flat_floor=flat.floor, new_status=new_status, new_price=new_price)
            notify.send_sms_notification(flat=flat, status_change=True, price_change=True)
        elif new_status != flat.status:
            db_session.update_flat(flat_floor=flat.floor, new_status=new_status)
            notify.send_sms_notification(flat=flat, status_change=True, price_change=False)
        elif new_price != flat.price:
            db_session.update_flat(flat_floor=flat.floor, new_price=new_price)
            notify.send_sms_notification(flat=flat, status_change=False, price_change=True)
        else:
            log(logging.INFO, f'Flat #{flat.flat_id} at floor {flat.floor} scanned successfully. No changes detected!')
    log(logging.INFO, '*** Scan session completed! ***\n')
