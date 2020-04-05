# seekを使って移動する
# 何文字目から読み込みたいのか
# 文字列をさかのぼって取得する時に使われる

s = """\
AAA
BBB
CCC
DDD
EEE
"""

# 書き込み
# with open('test.txt', 'w') as f:
#     f.write(s)

# 読み込み
with open('test.txt', 'r') as f:
    # f.tell読み込んだ文字列の何番目にいるかを取得（最初は0）
    print(f.tell())
    print(f.read(1))
    # 位置を移動
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
