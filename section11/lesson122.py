# ロギング　ロガー
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

import lesson122logtest

# ロギングの基本設定(infoレベルを指定)
logging.basicConfig(level=logging.INFO)


# ロガーはロギングの設定を引き継いで、特定の処理にだけログの設定を変更することができる
# 現在のロギングの情報を取得(引数はファイル名)
logger = logging.getLogger(__name__)
logging.info('from main')

# ロガーでもロギングのレベルを変更することができる
# ロギングの設定を DEBUG に変更
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

# 他ファイルから呼び出す
lesson122logtest.some_func()
