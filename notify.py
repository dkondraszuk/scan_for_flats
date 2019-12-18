import os
from my_logger import log
from twilio.rest import Client
import logging

FROM_NUMBER = '+12248032736'
TO_NUMBER = '+48796055524'

ACCOUNT_SID = 'AC06f573195bc04ffb7317d7f0c2f7ef31'
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

msg = 'Test msg'

message = client.messages.create(body=msg, from_=FROM_NUMBER, to=TO_NUMBER)


def send_sms_notification(flat, status_change=True, price_change=False):
    global msg
    if status_change and price_change:
        msg = f"Howdy Dawe! Flat {flat.flat_id} at {flat.floor} floor changed its status " \
              f"to '{flat.status.upper()}' and price to {flat.price} PLN."
    elif status_change:
        msg = f"Howdy Dawe! Flat {flat.flat_id} at {flat.floor} floor changed its status to '{flat.status.upper()}'."
    elif price_change:
        msg = f'Howdy Dawe! Flat {flat.flat_id} at {flat.floor} floor changed its price to {flat.price} PLN.'
    log(logging.INFO, 'Message sent: {}'.format(message.sid))
