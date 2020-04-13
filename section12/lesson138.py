# MySQl
import os
import mysql.connector

# forego run python lesson138.pyで.envファイルの環境変数を読み込ませることが可能
user_name = os.environ['USER_NAME']

# コネクションオブジェクトの作成
# 引数：host=PCのURL、本当はuser="",password=""を設定する必要があるが、今回は見送り
# user='root'で接続すると、なんでも作れる
# conn = mysql.connector.connect(host='127.0.0.1', user=user_name)

# カーソルの作成
# cursor = conn.cursor()

# SQL文の処理 DBの作成
# cursor.execute(
#     'CREATE DATABASE test_mysql_db138'
# )

# cursor.close()
# conn.close()

# 上記で作成したDBに接続する
conn = mysql.connector.connect(
    host='127.0.0.1', user=user_name, database='test_mysql_db138')

# カーソルの作成
cursor = conn.cursor()

# SQL文の処理 テーブルの作成
# 複数行に跨がる場合の書き方
# NOT NULL:必ずいれる、varchar(14):14文字以内の文字列
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))'
#                )

# データの挿入
# cursor.execute('INSERT INTO persons(name) values("Mike")')
# cursor.execute('INSERT INTO persons(name) values("Naoya")')

# データの更新
# cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')

# データの削除
cursor.execute('DELETE FROM persons WHERE name = "Michel"')

# commit()を実行しないとDBの変更はされない
conn.commit()

# データの取得
cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)


cursor.close()
conn.close()
