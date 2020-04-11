# Email送信

"""
今回は@hotmailで例を示したが、もちろん@gmailも可能
手順は検索して確認する
"""

from email import message
import smtplib

import config

smtp_host = 'smtp.live.com'
smto_port = 587


# 送り主
from_email = 'xxx@hotmail.com'

# 送り先
to_email = 'yyy@hotmail.com'

# 送り主のmailアカウントにログインするための情報
username = 'xxx@hotmail.com'
password = 'fjaiegremsotijp'


# メッセージのオブジェクトを作成
msg = message.EmailMessage()

# メール本文
msg.set_content('Test email')

# メール件名
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email


# メール送信
server = smtplib.SMTP(smtp_host, smto_port)

# 今からserverと通信を始めると宣言
server.ehlo()

# serverとセキュアな通信を開始
server.starttls()

# もう一度serverと通信を始めると宣言
server.ehlo()

# ログイン情報を渡す
server.login(username, password)

# ログイン情報が認証されたら、メールを送信
server.send_message(msg)

# serverとの通信終了
server.quit()
