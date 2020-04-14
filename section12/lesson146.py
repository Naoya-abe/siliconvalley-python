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
