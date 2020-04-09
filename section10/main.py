# クロージャー
def base(x):
    def plus(y):
        return x + y
    return plus


# functionが返されただけなので実行はされていない
plus = base(10)
print(plus(10))
print(plus(20))


# グローバル変数で定義すると後々書き換えられるかもしれない。
# クロージャーを使ってうまく対応する
i = 0


def add_num():
    def plus(y):
        return i + y
    return plus


i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))

# import roboter.controller.conversation

# # bad
# # roboter.controller.conversation.talk_about_restaurant()


# class MainError(Exception):  # エラーを継承して自分なりのエラーを作成する
#     pass


# def main():  # good
#     roboter.controller.conversation.talk_about_restaurant()
#     raise MainError('error')
#     # 全てのエラーを記述しない
#     # except Exception as exc:
#     #     print(exc)


# # リスト内包括は無理に長く書かない
# x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]

# # dict型
# d = {'key1': 'value1', 'key2': 'value2'}
# # bad
# if 'key1' in d.keys():
#     print('test')

# # good dのみでkeyの判定をしてくれるので、.key()はいらない
# if 'key1' in d:
#     print('test')

# # dict型の展開では変数名がわかりやすく
# for name, count in d.items():
#     print(name, count)


# if __name__ == "__main__":
#     main()


# # ジェネレーターの方がアプリケーションの速度が早くなる
# def t():
#     # num = []
#     for i in range(10):
#         yield i
#         # num.append(i)
#     # return num


# for i in t():
#     print(i)


# def other_func(f):
#     print(f(10))


# # lambda：短い関数ならlambdaを使おう
# other_func(lambda x: x*2)


# def test_func(x):
#     return x * 2


# other_func(test_func)

# if文 一行で書けたりする
# y = None
# x = 1 if y else 2
