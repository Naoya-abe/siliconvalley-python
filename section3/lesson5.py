# 文字列のインデックスとスライス

word = 'Python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print("############")
print(word[0:2])
print(word[:2])
print("############")
print(word[2:])

# 文字の書き換え
# エラー
# word[0] = "j"
# コピーして書き換える
word = 'j'+word[1:]
print(word)

# indexの長さ

n = len(word)
print(n)
