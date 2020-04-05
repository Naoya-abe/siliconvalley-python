# ファイルの作成

# ファイル作成(更新)
f = open('test.txt', 'w')

# ファイルに追加
# f = open('test.txt', 'a')

# ファイルに書き込み。こっちのほうが使われる
f.write('Test\n')

#  print関数で書き込みもできる    sep:単語の間の補完  end:文章の終わりに何を入れるか
print('My', 'name', 'is', 'Naoya', sep='#', end='!', file=f)

# ファイルclose
f.close()
