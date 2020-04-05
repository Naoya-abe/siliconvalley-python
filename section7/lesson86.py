# 抽象クラス
import abc

# あまり使われない


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # 継承するクラスで必ずdriveメソッドを実装するようにする
    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    # def drive(self):
    #     print('OK')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


baby = Baby()

# adultでdriveメソッドを実装していないので、エラーとなる。
adult = Adult()


car = Car()

car.ride(adult)
car.ride(baby)
