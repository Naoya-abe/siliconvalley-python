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

# defaultだとloggingのレベルがwarningまでなので、自分でレベルを指定する
# logging.basicConfig(level=logging.INFO)

# ファイルに出力したい場合
logging.basicConfig(filename='test.log', level=logging.INFO)

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
