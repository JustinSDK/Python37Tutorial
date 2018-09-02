import logging, sys

logger = logging.getLogger(__name__)
logger.addFilter(lambda record: 'Orz' in record.msg)

logger.log(logging.ERROR, '發生了 XD 錯誤')
logger.log(logging.ERROR, '發生了 Orz 錯誤')