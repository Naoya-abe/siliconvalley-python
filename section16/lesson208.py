"""
hashlibのハッシュ
ハッシュはpycriptと違い暗号の復号化が出来ない。
ユーザのログイン情報とかに使われる
ハッシュと暗号前の文字列の比較表があったら、簡単に機密情報が漏れるのでは？
saltやストレッチを用いて、セキュリティを強化する
同じファイルかどうかという判断にも使える
"""
import base64
import os
import hashlib

user_name = 'user_1'
user_pass = 'password'
db = {}

# ハッシュと暗号前の文字列の比較表があったら、簡単に機密情報が漏れるのでは？
# 回避するためにsaltというものを作る
salt = base64.b64encode(os.urandom(32))  # この記述は暗号化では定番


# def get_digest(password):  # この処理を1行でやってくれるhashlibのメソッドがある
#     password = bytes(password, 'utf-8')
#     # hashlibのsha256アルゴリズムを使って、16進数を用いた暗号化
#     # saltを追加してセキュリティを強化
#     digest = hashlib.sha256(salt + password).hexdigest()
#     # しかしsaltを何回も試されると、突破されることがある
#     # その時はストレッチを使う。このforループを何回行ったかを知らないとハッカーはpasswordを知ることはできない
#     # ハッシュのハッシュを作成するので、簡単に突破されない
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
#         print(digest)
#     print(digest)
#     return digest

# get_digest()の処理を簡略化してくれる
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000
)

db[user_name] = digest

# db[user_name] = get_digest(user_pass)
# print(db[user_name])


def is_login(user_name, password):
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 10000
    )
    return digest == db[user_name]
    # return get_digest(user_pass) == db[user_name]


print(is_login(user_name, user_pass))
