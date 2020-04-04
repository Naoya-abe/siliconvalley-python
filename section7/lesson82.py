# メソッドのオーバーライドとsuperによる親のメソッドの呼び出し


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')
        print('#################')


class ToyotaCar(Car):
    def run(self):  # メソッドのオーバーライド
        print('fast')


class TeslaCar(Car):
    # __init__をオーバーライドする時
    def __init__(self, model='Model S', enable_auto_run=False):
        # super()で、親クラスのメソッドを呼び出す。親への要請
        super().__init__(model)
        # 追加でクラス変数を付け足すことができる。
        self.enable_auto_run = enable_auto_run

    def run(self):  # メソッドのオーバーライド
        print('supe fast')

    def auto_run(self):
        print('auto_run')
        print('################')


car = Car()
car.run()


toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()


tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
