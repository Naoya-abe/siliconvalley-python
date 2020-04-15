"""
json
データ送受信の形式
XMLよりも手軽に使える

{
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"},
    ]
}

基本的にpythonのスクリプト内でしようする場合は「dumps」、「loads」のように「s」がつく
jsonファイルの読み書きをしたい場合は「dump」「load」のように「s」はつかない
"""

import json

j = {
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"},
    ]
}

print(j)
print('###################')

# jsonに変換
print(json.dumps(j))
print('###################')

# jsonファイルの書き込み
with open('test152.json', 'w') as f:
    # 書き込みは「dump」なので注意
    json.dump(j, f)

# jsonファイルの読み込み
with open('test152.json', 'r') as f:
    print(json.load(f))
