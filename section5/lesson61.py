# 辞書包括表記

# リストから辞書型を作る

w = ['mom', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

# 辞書包括表記を使わない場合
for x, y in zip(w, f):
    d[x] = y

print(d)
print('###################################')


# 辞書包括表記を使う場合
g = {x: y for x, y in zip(w, f)}
print(g)
