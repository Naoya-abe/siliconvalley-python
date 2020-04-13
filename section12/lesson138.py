# MySQl

import mysql.connector

# コネクションオブジェクトの作成
# 引数：host=PCのURL、本当はuser="",password=""を設定する必要があるが、今回は見送り
# user='root'で接続すると、なんでも作れる
conn = mysql.connector.connect(host='127.0.0.1', user='root')

# カーソルの作成
cursor = conn.cursor()

# SQL文の処理
cursor.execute(
    'CREATE DATABASE test_mysql_db138'
)

cursor.close()
conn.close()
