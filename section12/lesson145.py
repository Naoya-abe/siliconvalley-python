"""
MongoDB NonSQL
ドキュメント指向DB
データの保存はJson形式
SQLほど複雑な検索はできないが、アップデータだけなど、複雑な検索機能を使わないなら、こちらの方が早い

DBを保存するディレクトリを作成する
mkdir ./data/db

pip install pymongo
"""

import datetime

from pymongo import MongoClient

# client作成
client = MongoClient('mongodb://localhost:27017')

# DBの作成
db = client['test_db145']

# dataの作成
stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'date': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'date': datetime.datetime.utcnow()
}

# tableの作成（tableの概念はないが）
db_stacks = db.stacks

# dataの追加
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))

# print("###########################")

# dataの読み込み。 idで検索する際には、'_id'としてObjectIdの形式で渡す
# print(db_stacks.find_one({'_id': stack_id}))

# print("###########################")

# nameで検索
# print(db_stacks.find_one({'name': 'customer1'}))

# stack2の追加
# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# tableの全てのデータを取得 forループで回すことで
# for stack in db_stacks.find():
# print(stack)

# 時間でフィルターをかける。 $lt=前 $gt=後
# now = datetime.datetime.now()
# for stack in db_stacks.find({'date': {'$gt': now}}):
#     print(stack)

# dataのアップデート
# db_stacks.find_one_and_update(
#     {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
# )

print(db_stacks.find_one({'name': 'YYY'}))

# dataの削除
db_stacks.delete_one({'name': 'YYY'})

print(db_stacks.find_one({'name': 'YYY'}))
