# enumerate関数

# for文の中でリストのindex番号を取得する

# enumerate関数を使わない場合
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1
else:
    print('################')

# enumerate関数を使う場合
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
