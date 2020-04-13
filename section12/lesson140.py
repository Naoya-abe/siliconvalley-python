"""
DBM：Pythonの標準ライブラリのDB
キャッシュなど簡易的なものを扱いたい
"""

import dbm


# with dbm.open('cache', 'c') as db:  # 'c'なければ書き込みする
#     # dict型で書き込むことができる
#     db['key1'] = 'value1'
#     db['key2'] = 'value2'
#     db['key3'] = 1 int型は保存できない

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))  # 出力：b'value1'　先頭のbはバイナリのb
