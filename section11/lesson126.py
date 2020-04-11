# ロギングの書き方

import logging

logger = logging.getLogger(__name__)

# 普通に書く場合もある
logger.error('Api call is failed')

# dict型で書く方法もある
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})

"""
なぜdict型で書くのか？
log解析のソフトウェアでkey、valueを用いた検索ができるようになるから

logの書くべき場所
重要な機能の前後

Ex)
logger.info({
    'action': 'save',
    'status': 'run'
})

    重要な処理

logger.info({
    'action': 'save',
    'status': 'success'
})

"""
