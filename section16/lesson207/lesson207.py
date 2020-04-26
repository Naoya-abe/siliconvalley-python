"""
pycryptoの暗号化と復号化
暗号化の知識がないと理解しにくいので、以下のキーワードで検索すること
AES, iv, padding

暗号化に興味ない人は、今回のようなパターンを覚えておけばOK!
encryptとdecryptメソッド
"""
import string
import random

from Crypto.Cipher import AES

# 暗号化Keyの作成
# string.ascii_lettersからランダムに,AES.block_size(16)の文字を抽出
# print(AES.block_size)
# print(string.ascii_letters)
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# print(key)

# ブロックの暗号化（暗号化は16文字ごとのブロックでなければならない）
# 初期ベクトル(ivを用いて、最初のブロックを暗号化する。これも16文字)
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# print(key, iv)

# ciperオブジェクトの作成。AES.new(暗号化key, アルゴリズム, 暗号化の初期ベクトル)
# plain_text = 'fjioajeios'
# cipher = AES.new(key, AES.MODE_CBC, iv)

# plaintextも16文字のブロックでなければいけないので、足りない分の計算
# len(plaintext) % AES.block_size = 暗号化したい文字列の長さを16で割ったあまり
# padding_length = 16文字に足りない文字の個数
# padding_length = AES.block_size-len(plain_text) % AES.block_size

# plaintextも16文字のブロックでなければいけないので、足りない分の追加
# plain_text += chr(padding_length) * padding_length

# 暗号化
# cipher_text = cipher.encrypt(plain_text)
# print(cipher_text)

# 復号化の過程
# cipher2 = AES.new(key, AES.MODE_CBC, iv)

# 復号化
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text)
# print(decrypted_text[-1])

# 暗号化するために追加した分の文字列を取り除く
# print(decrypted_text[:-decrypted_text[-1]])

# ファイルの暗号化と復号化
# 暗号化
with open('plain.txt', 'r') as f, open('enc.dat', 'wb') as e:
    plain_text = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size-len(plain_text) % AES.block_size
    plain_text += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plain_text)
    e.write(cipher_text)

# 復号化
with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))
