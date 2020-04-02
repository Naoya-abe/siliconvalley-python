# 辞書型のコピー

# NG
x = {'a': 1}
y = x
y['a'] = 1000
print(y)
print(x)
print('#############')

# OK
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(y)
print(x)
