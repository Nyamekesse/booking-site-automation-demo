import logging
import os
import sys

logs = os.path.join(os.getcwd(), 'logs')

if not os.path.exists(logs):
    os.mkdir(logs)

# initializes logging
logging.basicConfig(filename=os.path.join(logs, 'logs.log'), level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

logger = logging.getLogger(__name__)


def my_handler(type, value, tb):
    logger.exception(value)


sys.excepthook = my_handler
