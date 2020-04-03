# 例外処理
l = [1, 2, 3]
i = 0

"""
- エラーが発生した場合にexceptを実行する　
- jsのtry{}catch{}みたい
- elseはtryがエラーなく終了したら、実行する
- finallyはエラーがあってもなくても、必ず最後に実行したい処理
"""

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')
