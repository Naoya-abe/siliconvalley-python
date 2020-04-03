# 独自例外の作成

# 自分でエラーを発生させる
# raise IndexError('test error')


# 例


class UppercaseError(Exception):
    pass


def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

"""
独自の例外を作成することで、開発が楽になる
"""
