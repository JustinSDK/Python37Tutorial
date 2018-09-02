import logging

logging.basicConfig(filename ='openhome.log')

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('errors.log'))

logger.log(logging.ERROR, 'ERROR 訊息')


