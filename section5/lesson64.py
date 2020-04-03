# 名前空間とスコープ

# グローバル変数
animal = 'lion'


# 関数内からグローバル変数にアクセスはできる


def f():
    print(animal)


f()
print('######################')


# 関数内だけで代入もできる

def g():
    animal = 'pig'
    print('local :', animal)


g()

print('global :', animal)
print('######################')


# globalの変数を関数内で書き換えたい時

def h():
    global animal
    animal = 'dog'
    print('local', animal)


h()
print('global', animal)
print('######################')


# 関数内で宣言されている変数一覧を見る


def j():
    animal = 'cat'
    print('local', locals())


j()
print('######################')
