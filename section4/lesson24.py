# 辞書型

d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print('############')

# 値の取り出し
print(d['x'])
print(d['y'])
print('############')

# 値の変更
d['x'] = 100
print(d)
print('############')

# 値の追加
d['z'] = 300
print(d)
print('############')

# keyが数値でもOK
d[1] = 10000
print(d)
print('############')

# その他の宣言方法
p = dict(a=10, b=20)
print(p)
