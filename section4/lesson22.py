# タプルのアンパッキング（展開）

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple  # x, y = 10, 20 と一緒
print(x, y)
print('####################')

#　2つ程度なら見やすい
min, max = 0, 100
print(min, max)
print('####################')

# 数が多くなると見にくい
a, b, c, d, e, f = 1, 3, 6, 73, 7, 'Mike'
print('####################')

# 数字の入れ替えにtupleを利用できる
# tupleを使わない場合
i = 10
j = 20
print('i =', i)
print('j =', j)
tmp = i
i = j
j = tmp
print('i =', i)
print('j =', j)
print('####################')

# tupleを使う場合
a = 100
b = 200
print('a =', a)
print('b =', b)
a, b = b, a  # 数値の入れ替え処理が3行から1行に
print('a =', a)
print('b =', b)
print('####################')
