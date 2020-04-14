"""
memcached
メモリ内にデータのキャッシュを作成し、直接DBにアクセスする回数を減らす（高アクセスのデータに使う）
データの読み込みスピード向上、DBの負荷減少
インストール brew install memcached, pip install python-memcached
起動 memcached -vv
"""
import sqlite3
import time

import memcache

# クライアントを用意（どこのポートで使うか）
db = memcache.Client(['127.0.0.1:11211'])

# データのセット (key,value,timeout(Sec))
# db.set('web_page', 'value1', time=3)
# time.sleep(1)
# print(db.get('web_page'))

# valueの増加
# db.set('counter', 0)
# db.incr('counter', 1)
# db.incr('counter', 1)
# db.incr('counter', 1)
# print(db.get('counter'))

# sqliteとmemcachedを組み合わせる
conn = sqlite3.connect('test_sqlite141.db')
curs = conn.cursor()
# curs.execute(
#     'CREATE TABLE persons(employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()


def get_employ_id(name):  # 社員の名前を元に社員番号を検索
    # まずはmemcachedを検索
    employ_id = db.get(name)
    if employ_id:
        return employ_id
    # memcachedになかったら、DBの検索
    curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
    person = curs.fetchone()  # tuple型でデータを取得する
    # DBにもデータがなかったらエラー出力
    if not person:
        raise Exception('No employ')
    employ_id, name = person
    # memcachedにデータを保存
    db.set(name, employ_id, 60)
    return employ_id


print(get_employ_id('Mike'))
print(get_employ_id('Naoya'))
