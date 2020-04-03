# InとNotの使い所

y = [1, 2, 3]
x = 1
z = 4

# xはyの中に入っているか？
if x in y:
    print('in')
else:
    print('not')

if z not in y:
    print('not in')
else:
    print('in')

is_ok = True

# 直接booleanの判定をする時に「not」は使われる
if not is_ok:
    print('not')
else:
    print('OK')
