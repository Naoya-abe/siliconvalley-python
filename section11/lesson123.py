# ロギング　ハンドラー

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

import lesson123logtest

# ロギングの基本設定(infoレベルを指定)
logging.basicConfig(level=logging.INFO)


# ロガーはロギングの設定を引き継いで、特定の処理にだけログの設定を変更することができる
# 現在のロギングの情報を取得(引数はファイル名)
logger = logging.getLogger(__name__)
logging.info('from main')

# 他ファイルから呼び出す
lesson123logtest.some_func()
