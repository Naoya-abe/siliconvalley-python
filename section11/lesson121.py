"""
ロギングとは、起こった出来事についての情報などを一定の形式で時系列に記録・蓄積すること。
そのように記録されたデータのことを「ログ」（log）という。

CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging


# logging.basicConfig(level=logging.INFO)

# フォーマットを指定して出力
# https://docs.python.org/ja/3/howto/logging.html

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)
# 出力：INFO:root:info test test2 → INFO:info test test2 → 2020-04-11 09:24:47,779:info test test2

# loggingの出力
# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# 文字列を指定して出力
# logging.info('info %s %s' % ('test', 'test2'))

# カンマで区切る方法もあり
logging.info('info %s %s', 'test', 'test2')
