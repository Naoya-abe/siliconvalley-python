import csv
import os

from termcolor import colored

from roboter import user_name

print(colored('======================================', 'green'))
print(colored('Hello, I am Roboko. What is your name?', 'green'))
print(colored('======================================', 'green'))

user_name = input("Please enter your name : ")

# おすすめが入る
if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'r') as csv_file:
        restaurants = {}
        reader = csv.DictReader(csv_file)

        # dict型でcsvファイルのデータを抽出
        for row in reader:  # str型で返ってくるので、int型に修正
            restaurants[row['Name']] = int(row['Count'])

        # valueの降順でソート（リストで返ってくる。Ex:[(,),(,),....]）
        sorted_restaurants = sorted(restaurants.items(),
                                    key=lambda x: x[1], reverse=True)

        # 最終的にこの辞書型を展開して、csvファイルに書き込む
        new_restaurants = {}

        # [(,),(,)...]を展開する
        for restaurant in sorted_restaurants:
            restaurant_name = restaurant[0]
            restaurant_count = restaurant[1]

            while True:
                print(colored('======================================', 'green'))
                print(
                    colored('Hi {}! I recommend you {} restaurant.'.format(user_name, restaurant_name), 'green'))
                print(colored('Do you like it? [y/n]', 'green'))
                print(colored('======================================', 'green'))
                answer = input('Please answer :').capitalize()
                # Yesの場合にcountを1増やす
                if answer == 'Yes' or answer == 'Y':
                    new_count = restaurant_count + 1
                    break
                elif answer == 'No' or answer == 'N':
                    new_count = restaurant_count
                    break
                else:
                    print(colored('Please answer "Yes" or "No"', 'red'))

            new_restaurants[restaurant_name] = new_count

    # csvファイルに追記 with openの中にfor文を書かないと、書いたデータが削除される
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in new_restaurants.items():
            writer.writerow({'Name': k, 'Count': v})


print(colored('======================================', 'green'))
print(colored('{}, which restaurant do you like ?'.format(user_name), 'green'))
print(colored('======================================', 'green'))

restaurant_name = input("Plese enter restaurant : ")

print(colored('======================================', 'green'))
print(colored('Roboko: Thank you so much {}!'.format(user_name), 'green'))
print('\n')
print(colored('Have a good day!', 'green'))
print(colored('======================================', 'green'))

if os.path.exists('ranking.csv'):
    with open('ranking.csv', 'r') as csv_file:
        # csvファイルの読み込み
        restaurants = {}

        # forループの中でrestaurantsに新しくkeyとvalueを追加することができなかったので
        # この変数を宣言して、このdict型の中で新規のkeyとvalueを追加して、csvファイルに出力する
        new_restaurants = {}
        reader = csv.DictReader(csv_file)

        # dict型でcsvファイルのデータを抽出
        for row in reader:  # str型で返ってくるので、int型に修正
            restaurants[row['Name']] = int(row['Count'])

        # 値の代入
        # 以下のコピーの仕方だと参照渡しになって
        # new_restaurantsの値を変更した時にrestaurantsの値も変更されるので注意
        # new_restaurants = restaurants

        # dict型のコピーはこうする
        new_restaurants = restaurants.copy()

        # 入力値とcsvファイルのkeyを比較
        for k, v in restaurants.items():
            # 同じ名前のレストランを入力されたらカウントを1増加させ、新しいdict型に追加
            if k == restaurant_name:
                new_restaurants[k] = v + 1
            else:
                # 異なる名前のレストランが入力されたら、カウントを1として新しいdcit型に追加
                new_restaurants[restaurant_name] = 1

    # csvファイルに書き込み
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in new_restaurants.items():
            writer.writerow({'Name': k, 'Count': v})

else:
    with open('ranking.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': restaurant_name, 'Count': 1})
