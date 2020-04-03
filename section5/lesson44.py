# range関数

# 0~9の数字を出力するプログラム

# for文を使った場合
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)
else:
    print('###############')

# range関数を使った場合

# 0からスタートして9まで数字を出力
for i in range(10):
    print(i)
else:
    print('###############')

# 2からスタートして9まで数字を出力
for i in range(2, 10):
    print(i)
else:
    print('###############')

# 2からスタートして3個飛ばしで9まで数字を出力
for i in range(2, 10, 3):
    print(i)
else:
    print('###############')

# for文で繰り返す数が予め決まっている場合は
for i in range(10):
    print(i)
else:
    print('###############')

# rangeの中の値を必要としないとき
for _ in range(10):
    print('hello')
else:
    print('###############')
