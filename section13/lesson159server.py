"""
XML RPC
clietからserverで関数を用意しておいて、clientから呼び出す
結果はclientに返す

大量にアクセスをさばく場合にはREST
XMLRPCは簡単に処理できる。
ネットワークの遅延の問題ある
社内インフラとかならOK!
"""

from xmlrpc.server import SimpleXMLRPCServer


with SimpleXMLRPCServer(('127.0.0.1', 8000)) as server:
    # 関数を定義
    def add_num(x, y):
        return x + y

    # 関数の登録 (serverで作成した関数、"client側から呼び出す名前")
    server.register_function(add_num, "add_num")
    server.serve_forever()
