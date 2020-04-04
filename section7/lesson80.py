# コンストラクターとデストラクター
class Person(object):
    # コンストラクター：classを作成する際に呼ばれるもの
    def __init__(self, name):  # selfは自分自身nameは引数
        self.name = name  # 引数のname、自身のnameに代入する
        print(self.name)

    def say_something(self):  # selfを用いて、自分自身に保持した値を取得していく
        print('I am {}. hello'.format(self.name))
        self.run()  # 自身のメソッドにもアクセスできる

    def run(self):
        print('run')

    # デストラクター：オブジェクトが使われなくなる時に呼ばれるもの
    def __del__(self):
        print('goodbye')


# personが作られた時に「__init__」メソッドが実行される
person = Person('Mike')
print('###################')
person.say_something()
print('###################')
person.run()
# 明示的にデストラクターを呼びたいときは
del person
print('###################')
# ここでデストラクターが呼ばれる

