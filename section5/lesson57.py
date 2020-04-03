# デコレーター：ある関数に機能を付け加えたいとき


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# このデコレータを使うと明示
@print_info
def add_num(a, b):
    return a+b


# デコレータの使い回しも可能
@print_info  # 先にprint_infoを実行　
@print_more  # 今回のケースではstartが呼び出されて、次のfuncが呼び出された時にprint_moreに行く
def sub_num(a, b):
    return a-b


r = add_num(10, 20)
print(r)

r = sub_num(20, 10)
print(r)


# f = print_info(add_num)
# r = f(10, 20)
# print(r)
