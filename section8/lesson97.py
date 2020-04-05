# CSVファイルへの書き込みと読み込み
import csv

# csvファイルの書き込み
with open('test.csv', 'w') as csv_file:
    # ヘッダーの名前を入力
    fieldnames = ['Name', 'Count']
    # csvに書き込むためのオブジェクトの作成
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # ヘッダーの作成
    writer.writeheader()
    # ディクショナリ形式で実際に値を書き込む
    writer.writerow({'Name': 'a', 'Count': 1})
    writer.writerow({'Name': 'b', 'Count': 2})

# このファイルを開く場合はterminal”open test.csvと入力”

# csvファイルの読み込み
with open('test.csv', 'r') as csv_file:
    # csvを読み込む -> DictReader
    reader = csv.DictReader(csv_file)
    for row in reader:
        # それぞれのヘッダーに対応する値を取得
        print(row['Name'], row['Count'])
