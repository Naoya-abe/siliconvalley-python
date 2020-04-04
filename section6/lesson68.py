# import文とAS


# 方法１：package.fileで取得する
# import lesson_package.utils68
# r = lesson_package.utils68.say_twice('hello')

#　一番いい
# 方法２：from package import file で取得する
# from lesson_package import utils68
# r = utils68.say_twice('hello')

# あまり好まれていない
# 方法２-1：from package import file as name で取得する
from lesson_package import utils68 as u
r = u.say_twice('hello')
print(r)

# あまり好まれていない
# 方法3：from package.file import function で取得する
# from lesson_package.utils68 import say_twice
# r = say_twice('hello')
# print(r)

# 方法１か方法２が主流
# 会社によって違うので、その会社のルールに従う
