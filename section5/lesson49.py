# 関数の引数と返り値の宣言

# プログラマーにはわかりやすいけど、Python自体がエラーは出さない


def add_num(a: int, b: int) -> int:
    return a+b


# OK
r = add_num(10, 20)
print(r)
print('###############')

# NG
r = add_num("10", "20")
print(r)
