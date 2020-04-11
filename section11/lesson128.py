# 添付ファイルEmail送信

"""
今回は@hotmailで例を示したが、もちろん@gmailも可能
手順は検索して確認する
"""

from email import message
from email.mime import multipart
from email.mime import text
import smtplib

import config

smtp_host = 'smtp.live.com'
smto_port = 587

# config
from_email = 'xxx@hotmail.com'
to_email = 'yyy@hotmail.com'
username = 'xxx@hotmail.com'
password = 'fjaiegremsotijp'

# msgオブジェクトの作成
msg = multipart.MIMEMultipart()
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

# メールテキスト plainテキストであることを明記
msg.attach(text.MIMEText('Test email', 'plain'))

# 添付ファイルの作成
with open('lesson.py', 'r') as f:
    # 読み込んだファイルを添付する
    attachment = text.MIMEText(f.read(), 'plain')
    # ファイルをどのようにして送信するかheaderに記載
    attachment.add_header(
        # 添付ファイルであることを明記
        # インラインで送るか、添付ファイルで送るかの規格
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    # 添付
    msg.attach(attachment)


# メール送信
server = smtplib.SMTP(smtp_host, smto_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
