# クラスの初期化とクラス変数


class Person(object):
    def __init__(self, name):  # selfは自分自身nameは引数
        self.name = name  # 引数のname、自身のnameに代入する
        print(self.name)

    def say_something(self):  # selfを用いて、自分自身に保持した値を取得していく
        print('I am {}. hello'.format(self.name))
        self.run()  # 自身のメソッドにもアクセスできる

    def run(self):
        print('run')


# personが作られた時に「__init__」メソッドが実行される
person = Person('Mike')
print('###################')
person.say_something()
print('###################')
person.run()
