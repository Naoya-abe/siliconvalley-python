from lesson_package.tools import utils


def sing():
    return 'eaopgjespgitnrsbk'


def cry():
    return utils.say_twice('fmaenvsoruhtgrzmkgl')


# 他ファイルから読み込まれた時点で実行される
# そうしたくないときは
if __name__ == '__main__':
    print(sing())
    print('animal :', __name__)
