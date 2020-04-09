"""
config = 設定
今回はこれを作りたい

[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
# configファイルの読み書きに使える
import configparser

# configの定義
# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }

# configの書き込み
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

# configの読み取り アプリケーション内でconfigファイルを読み取りたいときは以下のようにする
config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])
