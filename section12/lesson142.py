"""
pickle
pythonのデータをそのままの形で保存する。
pythonだけなら、そのまま保存できるので良い。
他の言語との互換性はない。
"""

import pickle


class T(object):
    def __init__(self, name):
        self.name = name


data = {
    'a': [1, 2, 3],
    'b': ('test', 'test'),
    'c': {'key': 'value'},
    'd': T('test')
}

# バイナリファリルとして書き込み
with open('data142.pickle', 'wb') as f:
    # dataをfに書き込み
    pickle.dump(data, f)

# バイナリファイルの読み込み
with open('data142.pickle', 'rb') as f:
    # データの読み込み
    data_loaded = pickle.load(f)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))
