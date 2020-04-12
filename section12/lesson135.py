"""
SQLite
軽量で、中小規模のアプリケーションであれば使われる！
"""

import sqlite3

# DBに接続
# conn = sqlite3.connect('test_sqlite135.db')

# 練習用で何度もSQL文を試したい場合にはメモリ上に一時的にDBを作る
conn = sqlite3.connect(':memory:')

# DBを操作するためのカーソルを宣言
curs = conn.cursor()

# 実際にDBに行う操作を記述
# SQL文を用いてテーブルを作成
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')

# DBにコミット（実際にDBに書き込まれる）
conn.commit()

# Tableに名前を追加
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

# Tableのデータを全て取得
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# Tableに名前を追加して取得
curs.execute('INSERT INTO persons(name) values("Nanct")')
curs.execute('INSERT INTO persons(name) values("Naoya")')
conn.commit()
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# データの書き換え
curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
# コミットを忘れるとプログラム上では置き換わっているが、DBに反映されていないので注意
conn.commit()
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# データの削除
curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# 接続終了
curs.close()
conn.close()
