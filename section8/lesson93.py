# ファイルの読み込み

s = """\
AAA
BBB
CCC
DDD
EEE
"""

# 書き込み
# with open('test.txt', 'w') as f:
#     f.write(s)

# 読み込み
with open('test.txt', 'r') as f:
    # 一気に全て読み込み
    # print(f.read())

    # 一行ずつ読み込み
    # while True:
    #     line = f.readline()
    #     print(line, end='')  # printは自動的に改行してくれる
    #     if not line:
    #         break

    # 文字数を指定して読み込み
    while True:
        chunk = 2  # 文字数を指定
        line = f.read(chunk)
        print(line)
        if not line:
            break
