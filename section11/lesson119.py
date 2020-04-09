"""
web_server:
    host: 127.0.0.1
    port: 80

db_server:
    host: 127.0.0.1
    port: 3306
"""
import yaml

# yamlファイルの書き込み
# with open('config.yml', 'w') as yaml_file:
#     yaml.dump({
#         'web_server': {
#             'host': '127.0.0.1',
#             'port': 80
#         },
#         'db_server': {
#             'host': '127.0.0.1',
#             'port': 3306
#         }
#     }, yaml_file)

# yamlファイルの読み込み
with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file)
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])
