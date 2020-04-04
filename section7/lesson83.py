# プロパティを使った属性の設定


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')
        print('#################')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model)
        # 外部からアクセスしてほしくないと明示的に示す場合：_をつける
        self._enable_auto_run = enable_auto_run
        # クラス変数をもたせる時に忘れない
        self.passwd = passwd

    # デコレーターで@propertyを指定して、読み取り専用にする
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # プロパティはある条件のときだけ値を更新できる仕様のときに使える
    # パスワードが一致した時など
    # プロパティーの値を書き換えたい場合：setterを使う
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('supe fast')

    def auto_run(self):
        print('auto_run')
        print('################')


# 変更できる
tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
# クラス変数を変更する
# tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)

# 勝手に変更されたくないときはどうするか → プロパティを使う！
