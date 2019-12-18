# Web scrapper used to monitor real estate price and availability

Project helps me to keep track of prices and availability of flats that I'd like to buy in the future.
It scans property developer's website and sends sms notification if any change was detected.
This way I am up to date with flats availability of my interest and can make decision in a right time :)

## Requirements:
* python3.6+
* AUTH_TOKEN environment variable set with your private Twilio token


## Libraries used in this project:
* requests (for sending HTTP requests)
* beautifulsoup4 (for scrapping HTML)
* sqlalchemy (with SQLite to store flats price and status)
* twilio (for sending sms notification)

## Install libraries (use only inside virtualenv):
* pip install -r requirements.txt
