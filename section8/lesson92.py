# withステートメントでファイルをオープンする

# withステートメントを使わない場合
# f = open('test.txt', 'w')
# f.write('Test\n')
# f.close()

"""
ファイルを開くとメモリを使うので、用がなくなったら閉じる
ファイルcloseを忘れないように、withステートメントを使うと良い
"""

# withステートメントを使う場合 closeをしなくても、fileをcloseしてくれる
with open('test.txt', 'w') as f:
    f.write('TEST\n')
