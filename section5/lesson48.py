# 関数定義

# まだ関数定義がされていないので関数が実行されない
# say_something()


def say_something():
    print('hi')


say_something()

print('################')


# 返り値が欲しい場合


def return_something():
    s = 'hi'
    return s


result = return_something()
print(result)
print('################')


# 引数を使う場合


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)
print('################')
