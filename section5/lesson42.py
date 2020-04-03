# for文とcontinue文とbreak文

some_list = [1, 2, 3, 4, 5]

# リストの中身を１つずつ出力

# while文を使用した場合
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

# for文を使用した場合
for j in some_list:  # some_listの値を順番に「j」に入れて実行する
    print(j)

# 文字列でもできる
for s in 'abcde':
    print(s)

# break、continueも使える
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    elif word == 'Mike':
        break
    print(word)
