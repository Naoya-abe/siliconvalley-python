import socket


"""
TCP通信
通信方式を指定してsocketをopen
socket.AF_INET:IPV4を指定, socket.SOCK_STREAM:TCP・IP
"""

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 50007))
#     # socketにコネクトしたらメッセージを送る
#     s.sendall(b'Hello')
#     # dataを取得
#     data = s.recv(1024)
#     print(repr(data))


"""
UDP通信
clientが受け取ったことを確かめない。
TCPと比べて信頼性が高くはないが
速さやリアルタイム性を求める通信に
使用されるプロトコル
"""

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', ('127.0.0.1', 50007))
