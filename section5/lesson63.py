# ジェネレーター内包表記


def g():
    for i in range(10):
        yield i


g = g()
print(next(g))
print(next(g))
print(next(g))
print("##################")
print(next(g))

# tupleではなくジェネレーターになる
b = (i for i in range(10))
print(type(b))

# tupleにしたい時
c = tuple(i for i in range(10))
print(type(c))
