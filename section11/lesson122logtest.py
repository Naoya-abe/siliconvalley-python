import logging

# 基本的にloggerを使って各機能のlogを出力する
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def some_func():
    logger.info('from logtest')
    logger.debug('from logtest debug')
