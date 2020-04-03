# クロージャー


def outer(a, b):
    def inner():
        return a+b

    return inner


f = outer(1, 2)  # この段階ではinner関数が入っているが実行はされていない
print(f)
r = f()  # ここで初めてinner関数が実行される
print(r)
print('#############')

"""
どのような場面で使われるのか？
関数をすぐに実行したくなく、関数を実行する前に様々な処理を行う際に使う
"""


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


# 先にpiの値のみを決めて、その後、状況に合わせてどちらを使うか決めることが可能
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
