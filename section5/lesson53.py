# キーワード引数の辞書化
# 引数が何個あっても「**」をつけるとキーワード引数を辞書化してくれる


def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    else:
        print('#############')


menu(entree='beef', drink='coffee')

# 一度辞書型を展開して引数にする
d = {'entree': 'pork', 'drink': 'ice coffee', 'dessert': 'ice'}
menu(**d)
