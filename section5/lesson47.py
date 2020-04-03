# 辞書型をfor文で使用する

d = {'x': 100, 'y': 200}
print(d.items())
print('###################')

# この場合Keyのみが出力される
for v in d:
    print(v)
else:
    print('#########')

# KeyとValueの両方を出力したい場合 -> itemsメソッドを使う
# tuppleのアンパッキングを利用
for k, v in d.items():
    print(k, ':', v)
