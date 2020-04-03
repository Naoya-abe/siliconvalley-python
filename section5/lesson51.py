# デフォルト引数で気をつけること

#


def test_func(x, l=[]):
    l.append(x)
    return l


y = [1, 2, 3]
r = test_func(100, y)
print(r)
print('#################')

y = [1, 2, 3]
r = test_func(200, y)
print(r)
print('#################')

r = test_func(100)
print(r)  # [100]

r = test_func(100)
print(r)  # [100,100]


# Pythonではリストをデフォルト引数に宣言するとバグの原因になるので避ける（参照渡しになる）
# default引数に空のリスト・ディクショナリを使用したい場合「None」を使う


def empty_list(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


s = empty_list(100)
print(s)
s = empty_list(100)
print(s)
