# 集合型

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)  # 重複がなくなる
print(type(a))
print('###############')

# 集合型同士の引き算
b = {2, 3, 3, 6, 7}
print(b)
print(a-b)
print(b-a)
print('###############')

# aかつb
print(a & b)  # +ではない
print('###############')

# aまたはb
print(a | b)
print('###############')

# aとbに存在しているが重複していないもの
print(a ^ b)
