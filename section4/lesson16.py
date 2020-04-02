# リスト型

# リストの値の取得
l = [1, 20, 4, 50, 2, 1, 2]
print(l[0])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])
print(len(l))
print("###########################")

# リストの値の取得（応用）
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# １つ飛ばし
print(n[::2])
# 後ろから
print(n[::-1])
print("###########################")

# リストのネスト
a = ['a', 'b', 'c']
b = [1, 2, 3]
z = [a, b]
print(z)
# ネストされているリストを取得
print(z[0])
print(z[1])
# ネストされているリストの値を取得
print(z[0][2])
print(z[1][0])
