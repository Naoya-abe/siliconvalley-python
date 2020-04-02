# 辞書型のメソッド

d = {'x': 10, 'y': 20}

# Key一覧の取得
print(d.keys())
print('###############')

# Value一覧の取得
print(d.values())
print('###############')

# dict型のオーバーライド
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)
print('###############')

# Valueの取得
print(d.get('x'))  # 当てはまるkeyが存在しない場合はNoneTypeを返す（空白？）
print('###############')

# Valueの取り出し
r = d.pop('x')
print(r)
print(d)
print('###############')

# Valueの削除
del d['y']
print(d)
print('###############')

# 型を残しつつKey:Valueを全削除
d.clear()
print(d)
print('###############')

# Keyがdict型の中に含まれているか判定
d = {'a': 100, 'b': 200}
print('a' in d)
print('j' in d)
print('###############')
