# リストのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3]

# 指定した値のindexの番号を取得
print(r.index(2))
# 指定した値のindexの番号を、指定したindex番号の後から取得　index(指定した値、検索開始index番号)
print(r.index(2, 2))

# 指定した値の個数
print(r.count(2))

# 検索
if 5 in r:
    print('exist')

# ソート
r.sort()
print(r)

# ソート（逆順）
r.sort(reverse=True)
print(r)

# ソート（逆順2）
r.reverse()
print(r)

# スプリット
s = 'My name is Mike.'
to_split = s.split(' ')  # 今回はスペースで区切ってリストを作成
print(to_split)

# ジョイン
x = ' '.join(to_split)  # 指定したリストをスペースで結合させる
print(x)
