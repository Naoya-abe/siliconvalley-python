s = 'test'
print(s)

print("I don't know")
# シングルクォートの中でシングルクォートは使えない
# print('I don't know')

print('hello.\nHow are you')
# 改行させたくないときは、「r」をつける
print(r'C:\name\name')

# 自動的に改行を入れる
print("####################")
print("""\
line1
line2
line3\
""")
print("####################")

# 文字列を演算子を使って連続で表示
print('Hi.' * 3)

# 長い文字列は見やすく2行に
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)
