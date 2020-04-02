# リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

# 値の書き換え
s[0] = 'X'
print(s)

# スライスで書き換え
s[2:5] = ['C', 'D', 'E']
print(s)

# スライスですべての要素を空にする
s[2:5] = []
print(s)

# スライスで全てを削除
s[:] = []
print(s)

print('######################################')

# リストのメソッド
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)

# 最後尾に値を追加
n.append(100)
print(n)

# 先頭に値を追加
n.insert(0, 200)
print(n)

# 最後尾の値を取り出す
n.pop()
print(n)

# 先頭の値を取り出す
n.pop(0)
print(n)

# 強力な削除
del n[0]
print(n)

# nを削除
del n

# nを再代入
n = [1, 2, 2, 2, 3]
print(n)

# 先頭から当てはまる値を削除
n.remove(2)
print(n)
n.remove(2)
print(n)
n.remove(2)
print(n)

# リストの結合
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)

x = a+b
print(x)

a += b
print(a)

# リストのメソッド
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(x)

x.extend(y)
print(x)
