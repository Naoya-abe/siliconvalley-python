# クラスの継承
# 最初に共通のクラスを定義して、そこから派生していけばコードがきれいになる


class Car(object):
    def run(self):
        print('run')
        print('#################')


class ToyotaCar(Car):
    pass  # 何もしない


class TeslaCar(Car):
    def auto_run(self):
        print('auto_run')
        print('################')


car = Car()
car.run()

# ToyotaCarにはrunを定義していないがCarから継承しているので使える
toyota_car = ToyotaCar()
toyota_car.run()

# クラスを継承して拡張もできる
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
