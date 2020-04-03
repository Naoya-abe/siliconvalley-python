# zip関数

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# それぞれ対応させて出力

# zip関数を使わない場合
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])
else:
    print('################')

# zip関数を使う場合
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
