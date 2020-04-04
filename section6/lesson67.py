# コマンドライン引数

import sys

print(sys.argv)

"""
terminalにて

入力
python lesson67.py option1 option2

出力
['lesson67.py', 'option1', 'option2']

"""

# terminalから値を渡してあげて出力
for i in sys.argv:
    print(i)
