"""
# Hbase
- ワイドカラム型のDB
- columnを横に増やしていくことができる
- インストール方法
    - $ brew cask install homebrew/cask-versions/adoptopenjdk8
    - $ brew install hbase
- 起動
    - To have launchd start hbase now and restart at login:
        brew services start hbase
      Or, if you don't want/need a background service you can just run:
        /usr/local/opt/hbase/bin/start-hbase.sh
- 操作
    - シェルスクリプトの起動
        - $ hbase shell
    - tableとcolumn familyの作成
        - create 'table', 'column family'
    - dataの追加
        - put 'table', 'row', 'column', 'value'
    - dataの読み込み（table内全て）
        - scan 'sns'
    - dataの読み込み（個別）
        - get 'table' 'row'
        - scan 'table', {COLUMNS => ['column']}
    - tableの削除
        - disable 'table'
        - drop 'table'
"""

# pythonのコードでhbaseを操る
# $ hbase thrift start
# $ pip install happybase
# $ pip freeze | grep happybase   出力：happybase==1.2.0

import happybase

# コネクションの作成
connection = happybase.Connection('localhost')

# コネクションの開通
connection.open()

# テーブル作成
connection.create_table(b'sns', {'blog': dict()})

# テーブルとコネクションの接続
table = connection.table(b'sns')

# テーブルにデータを追加
table.put(
    b'user1', {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccer': b'user1 about soccer'
    }
)

table.put(
    b'user2', {
        b'blog:soccer': b'user2 about soccer'
    }
)

# テーブルの情報取得
print(list(table.scan()))
print()
print(list(table.scan(row_prefix=b'user1')))
print()
print(list(table.scan(columns=[b'blog:soccer'])))

# テーブルの削除
connection.disable_table(b'sns')
connection.delete_table(b'sns')
