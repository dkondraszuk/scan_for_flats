import logging

LOG_TO_FILE = True
CONSOLE_FORMAT = '%(levelname)-8s| %(message)s'
FILE_FORMAT = '%(asctime)s | %(levelname)-8s | %(message)s'
DATE_FORMAT = '%d/%m/%Y %H:%M:%S'


logging.raiseExceptions = True

# create custom logger instance:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_formatter = logging.Formatter(fmt=CONSOLE_FORMAT)
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# create file handler, formatter and add to logger instance if specified:
if LOG_TO_FILE:
    file_formatter = logging.Formatter(fmt=FILE_FORMAT, datefmt=DATE_FORMAT)
    file_handler = logging.FileHandler(filename='failures.log', mode='a', encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

# log - this is the method we are using:
log = logger.log

if __name__ == '__main__':
    log(logging.DEBUG, "A quirky message only developers care about")
    log(logging.INFO, "Curious users might want to know this")
    log(logging.WARNING, "Something is wrong and any user should be informed")
    log(logging.ERROR, "Serious stuff, this is red for a reason")
    log(logging.CRITICAL, "OH NO everything is on fire")
