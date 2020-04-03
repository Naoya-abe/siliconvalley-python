# 関数内関数
# 関数内だけで使いたい処理がある場合


def outer(a, b):
    print(a, b)

    def plus(c, d):
        return c+d
    r = plus(a, b)
    print(r)


outer(1, 2)
