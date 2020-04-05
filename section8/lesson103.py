# datetime
import datetime
import time
import os
import shutil

now = datetime.datetime.now()

# default
print(now)

# 国際標準フォーマット
print(now.isoformat())

# 自分でフォーマットを指定
print(now.strftime('%d/%m/%Y-%H%M%S%f'))

# 年月日の表示
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%Y'))

# 時刻
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)

# 時間をずらして表示
d = datetime.timedelta(weeks=1)
# 一年前
d = datetime.timedelta(days=365)
d = datetime.timedelta(days=1)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(seconds=1)
d = datetime.timedelta(microseconds=1)
print(now-d)

# １秒間何もしない
print('########')
time.sleep(2)
print('########')

# ファイルのバックアップにも使える

file_name = 'date.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_&M_%S')))

with open(file_name, 'w') as f:
    f.write('date_test')
