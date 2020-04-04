# 標準ライブラリ
# url:https://docs.python.org/ja/3/library/index.html

# 今回はよく使うcollectionsを使ってみよう
from collections import defaultdict

# 特定のアルファベットの個数をカウントする

s = 'foearjgietsghnrfjbjr'
p = 'fjrifghnetsigulrshli'
w = 'fairgjfeorsgjrsbnjld'

# 方法1
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

# 方法2
g = {}
for q in p:
    g.setdefault(q, 0)  # Keyが存在しない時に使える
    g[q] += 1
print(g)

# 方法3

l = defaultdict(int)

for x in w:
    l[x] += 1
print(l)
