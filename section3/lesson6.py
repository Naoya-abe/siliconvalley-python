# 文字のメソッド

s = 'My name is Mike. Hi Mike.'
print(s)

#　引数に指定した文字から始まっているか？
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)
print("##############")

# 文字列が何番に含まれているか
print(s.find('Mike'))
print("##############")

# 文字列が何番に含まれているか（後ろから探すバージョン）
print(s.rfind('Mike'))
print("##############")

# 引数が文字列の中に何個含まれているか
print(s.count('Mike'))
print("##############")

# 先頭の文字を大文字にしてそれ以外は小文字
print(s.capitalize())
print("##############")

# すべての文字の先頭が大文字になる
print(s.title())
print("##############")

# 全てが大文字
print(s.upper())
print("##############")

# 全てが小文字
print(s.lower())
print("##############")

# 文字列の置き換え
print(s.replace('Mike', 'Nancy'))
print("##############")
