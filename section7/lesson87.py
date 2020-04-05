# 多重継承


class Person(object):
    def talk(self):
        print('talk')

    def run(self):  # こちらにもrunを追加すると...
        print('person run')


class Car(object):
    def run(self):
        print('car run')


# 複数のクラスを継承したい時。多重継承はあまりないほうが良い。設計が大事。
class PersonCarRobot(Car, Person):  # 継承するクラスに同名のメソッドがあった場合は、左側のメソッドが優先される
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()

person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()
