# 位置引数のタプル化

# 引数が何個あっても「*」をつけると位置引数をタプル化してくれる


def say_something(*args):
    print(args)
    for arg in args:
        print(arg)


say_something('Hi', 'Mike', 'Nancy')
