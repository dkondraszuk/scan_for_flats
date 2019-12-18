import logging
import os

from twilio.rest import Client

from my_logger import log

FROM_NUMBER = '+12248032736'
TO_NUMBER = '+48796055524'

ACCOUNT_SID = 'AC06f573195bc04ffb7317d7f0c2f7ef31'
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms_notification(flat, status_change=True, price_change=False):
    if status_change and price_change:
        msg = f"Howdy Dawe! Flat #{flat.flat_id} at {flat.floor} floor changed its status " \
              f"to '{flat.status.upper()}' and its price to {flat.price} PLN."
    elif status_change:
        msg = f"Howdy Dawe! Flat #{flat.flat_id} at {flat.floor} floor changed its status to '{flat.status.upper()}'."
    else:
        msg = f'Howdy Dawe! Flat #{flat.flat_id} at {flat.floor} floor changed its price to {flat.price} PLN.'

    message = client.messages.create(body=msg, from_=FROM_NUMBER, to=TO_NUMBER)
    log(logging.INFO, 'Message sent! ID: "{}". Content:\n"{}"'.format(message.sid, msg))
