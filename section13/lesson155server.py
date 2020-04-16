"""
# socket通信
    - TCP/IPと呼ぶ通信プロトコルを利用
    - プログラムの世界とTCP/IPの世界を結ぶ特別な出入り口
    - HTTP通信よりも低レイヤ
# TCP
    - トランスポート層
    - データの内容はおいといて、通信デバイス間での通信内容を確実に送受信するためのルール
# HTTP
    - アプリケーション層
    - TCPにさらにルールを追加して、送受信されるデータの形式や送受信タイミングを
      Webサイト閲覧に最適化する形に定められたルール
# ポートの種類
    - ウェルノウンポート番号(0-1023)
    - 登録済みポート番号(1024-49151)
    - 動的・プライベート ポート番号(49152-65535) 今回使うのはここ！
"""

import socket

"""
TCP通信
通信方式を指定してsocketをopen
socket.AF_INET:IPV4を指定, socket.SOCK_STREAM:TCP・IP
"""
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # hostとportを指定
#     s.bind(('127.0.0.1', 50007))
#     # 接続数
#     s.listen(1)
#     while True:
#         # 誰かが接続するまで待機、接続が確認できたら
#         # connectionとaddressを渡す
#         conn, addr = s.accept()
#         # 接続が終わったらsocketを閉じるようにwithを使う
#         with conn:
#             while True:
#                 # 1024というチャンクを受け取る
#                 # チャンク：分割されたデータ
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data: {}, addr: {}'.format(data, addr))
#                 # clientにデータを返す
#                 conn.sendall(b'Received' + data)

"""
UDP通信
clientが受け取ったことを確かめない。
TCPと比べて信頼性が高くはないが
速さやリアルタイム性を求める通信に
使用されるプロトコル
"""

# socket.SOCK_DGRAM：udp通信
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))
