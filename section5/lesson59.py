# ジェネレーター
# functionの中にyield
# returnを記述しない
# ループの状態を保持しているので、一旦ループを抜け出して、また元の位置に戻って、処理を再開できる
# 重たい処理を分割する


def counter(num=10):
    for _ in range(num):
        yield 'run'


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
