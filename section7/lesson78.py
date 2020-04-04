# クラスの定義
# (object)はなくてもいいが、書くのをおすすめ


class Person(object):
    def say_something(self):
        print('hello')


person = Person()
person.say_something()
