# 位置引数とキーワード引数とデフォルト引数


def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)
    print('#######################')


# 位置引数
# OK
menu('beef', 'beer', 'ice')
# NG 位置を間違えてしまう
menu('beef', 'ice', 'beer')

# キーワード引数
# OK 位置が間違っていても大丈夫
menu(entree='beef', dessert='ice', drink='beer')


# デフォルト引数：引数に指定がない場合、関数の中に定義された値が用いられる


def def_menu2(entree='beef', drink='wine', dessert='banana'):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)
    print('#######################')


def_menu2()
# もちろん書き換えも可能
def_menu2(entree='chicken', drink='beer')
