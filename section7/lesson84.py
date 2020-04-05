# クラスを構造体として扱う際の注意点


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')
        print('#################')


# class ToyotaCar(Car):
#     def run(self):
#         print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model)
        # __を２つつけると、アクセスできなくなる
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

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


tesla_car = TeslaCar('Model S', passwd='456')

# 新しく__enable_auto_runの属性が付け加えられてしまい、バグの原因になる
# class内の__enable_auto_runを更新している訳ではない
tesla_car.__enable_auto_run = 'XXXXXXXXXXXXXXXXXXX'
print(tesla_car.__enable_auto_run)  # 普通は、エラーが起こる

# クラスに値を追加するときは、元のクラスに何が入っているのかを確認してから実行すること


class T(object):
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)
