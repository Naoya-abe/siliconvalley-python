# ロギング フィルタ
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


logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):  # logging.Filterを継承してクラスを宣言
    def filter(self, record):  # Trueだったらlogして、Falseだったらlogしない
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)

# loggerにfilter機能を追加
logger.addFilter(NoPassFilter())
logger.info('from main')
# 誰かが間違ってパスワードなどをlogに残すようにしてしまった
# フィルタ機能を追加したので、出力されない
logger.info('from main password = "test" ')
