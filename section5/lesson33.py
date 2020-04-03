# if文

x = 0

# if文
if x < 0:
    print('negative')
elif x == 0:  # 先にでてきた方の処理が実行される
    print('zoro')
elif x == 0:
    print('positive')
else:
    print('positive')

print('################')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('a is positive')
