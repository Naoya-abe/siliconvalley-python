# 特殊メソッド
class Word(object):
    # 以下のようにメソッドの前後に__method__を"_"が２つついてるものが特殊メソッド
    def __init__(self, text):
        self.text = text

    # 文字列として呼ばれた時に実行される。結構使われる。
    def __str__(self):
        return 'Word!!!!!!!!'

    # 文字列の長さを取得
    def __len__(self):
        return len(self.text)

    # ２つのクラスを足し合わせる
    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    # ２つのクラスで持っている引数は等しいか
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('text')
w2 = Word('text')

print(w + w2)
print(w == w2)
