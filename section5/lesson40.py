# while else文

count = 0

while count < 5:
    print(count)
    if count == 1:
        break
    count += 1
else:
    print('done')

# else:whileループの中でbreakで終わらなかったら出力される
