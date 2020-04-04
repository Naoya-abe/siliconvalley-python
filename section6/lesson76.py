# importする際の記述の仕方

"""
一行ずつ書いていく
アルファベット順
標準ライブラリとサードパーティライブラリの間は一行開ける
自分たちのライブラリも一行開ける
"""

# 標準ライブラリ
import collections
import os
import sys

# サードパーティライブラリ
import termcolor

# 自作のライブラリ
import lesson_package

# localのファイル
import config

# ファイルの位置確認
print(collections.__file__)
