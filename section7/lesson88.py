# クラス変数
class Person(object):
    # オブジェクトが作成された時に保持される
    kind = 'human'

    def __init__(self, name):
        # 共通している self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()
print('################')


class T(object):
    # リストを共有するとバグにつながるので注意が必要
    # words = []

    # 共有されない方法
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def print_words(self):
        print(self.words)


c = T()
c.print_words()
c.add_word('Add')
c.add_word('Add2')
c.print_words()

d = T()
d.print_words()
d.add_word('Add3')
d.add_word('Add4')
d.print_words()

"""
クラス変数でリストを宣言すると、dのリストが
['Add', 'Add2', 'Add3', 'Add4'] のようにcのリストと共有されてしまうので注意。
"""
