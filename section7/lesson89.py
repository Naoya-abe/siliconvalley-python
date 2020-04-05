# クラスメソッドとスタティックメソッド
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    # 以下のように書けば、オブジェクト生成前でもメソッドを実行できる
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # あまり使わない。外部に関数としておいてもいいけど、そうすると何についてのaboutかわからなくなる。
    @staticmethod
    def about(year):
        print('about human {}'.format(year))


print(Person.about(1999))

# ()をつけるとオブジェクト作成と同時に__init__が実行され、xが保持される
a = Person()
print(a.x)
print(a.kind)
print(a.what_is_your_kind())

# ()をつけないとオブジェクト作成と同時に__init__が実行されず、xが保持されない
b = Person
print(b)

# エラー
# print(b.x)

# クラス内変数にはアクセスできる
print(b.kind)

# オブジェクトとして生成されていないので以下はエラーになる（@classmethod記述後はエラーにならない）
print(b.what_is_your_kind())
