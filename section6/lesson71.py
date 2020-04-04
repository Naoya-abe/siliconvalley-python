# ImportErrorの使い所

# パッケージを提供する際に古いバージョンと新しいバージョンが存在する時に使える
try:
    from lesson_package import utils
except:
    from lesson_package.tools import utils

r = utils.say_twice('word')
print(r)
