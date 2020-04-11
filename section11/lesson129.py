# SMTPハンドラーでログをEmail送信# 添付ファイルEmail送信

import logging
import logging.handlers


smtp_host = 'smtp.live.com'
smtp_port = 587

from_email = 'xxx@hotmail.com'
to_email = 'yyy@hotmail.com'
username = 'xxx@hotmail.com'
password = 'fjaiegremsotijp'

logger = logging.getLogger('email')

# criticalの際にメールを送るようにlevelを設定
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    # サーバー情報
    (smtp_host, smtp_port),
    # 送信元
    from_email,
    # 送信先
    to_email,
    # 件名
    subject='Admin test log',
    # 送信元のログイン情報
    credentials=(username, password),
    # 必要な場合記述 引数はstarttlsの中で使用されている。
    secure=(None, None, None),
    # タイムアウト[sec]
    timeout=20
))

logger.info('test')
logger.critical('critical')
