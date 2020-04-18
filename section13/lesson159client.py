"""
XML RPC
clietからserverで関数を用意しておいて、clientから呼び出す
結果はclientに返す

大量にアクセスをさばく場合にはREST
XMLRPCは簡単に処理できる。
ネットワークの遅延の問題ある
社内インフラとかならOK!
"""

import xmlrpc.client

with xmlrpc.client.ServerProxy('http://127.0.0.1:8000/') as proxy:
    print(proxy.add_num(200, 300))
