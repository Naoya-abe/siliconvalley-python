# ロギングハンドラー
# https: // docs.python.org/ja/3/library/logging.handlers.html

import logging

# 基本的にloggerを使って各機能のlogを出力する
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# この機能のlogだけ他のファイルに書き込みたい
h = logging.FileHandler('lesson123logtest.log')
logger.addHandler(h)


def some_func():
    logger.info('from logtest')
    logger.debug('from logtest debug')
