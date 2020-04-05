# テンプレート
# $のところに文字列を代入できる
# チーム内に
import string


with open('design/email_template.txt') as f:
    # このtはwithの外でも使える
    # テンプレートファイルを外部から読み込んで、デザイナーチームとプログラマーチームで作業を分けることが可能
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
