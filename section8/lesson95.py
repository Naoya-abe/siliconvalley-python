# 書き込み読み込みモード

s = """\
AAA
BBB
CCC
DDD
EEE
"""

# 書き込み：w
# with open('test.txt', 'w') as f:
# f.write(s)
# 書き込みの後にすぐに読み込みたい
# エラーが出る
# print(f.read())  # not readable

# 書き込み→読み込み：w+
with open('test.txt', 'w+') as f:
    f.write(s)
    """
    書き込みが終わった後は、ファイルの一番最後にいるので
    f.seek()を使ってファイルの先頭に戻る
    """
    f.seek(0)
    print(f.read())


# 読み込み→書き込み：r+（事前にファイルがないときはエラー）
with open('test2.txt', 'r+') as f:
    print(f.read())  # [Errno 2] No such file or directory: 'test2.txt'
    f.seek(0)
    f.write(s)
