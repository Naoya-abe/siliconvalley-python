# リストのコピー

# NG
i = [1, 2, 3, 4, 5]
j = i  # ここでは参照渡しがされている
j[0] = 100  # したがってiのリストの値も変化してしまう
print('j =', j)
print('i =', i)
print('##################################')

# OL
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)
print('##################################')

# 値渡しと参照渡し

# 値渡し
X = 20
Y = X
Y = 5
print(id(Y))
print(id(X))
print(Y)
print(X)
print('##################################')

# 参照渡し
X = ['a', 'b']
Y = X
Y[0] = 'c'
print(id(Y))  # idが一致する
print(id(X))  # idが一致する
print(Y)
print(X)
