# アスタリスクのインポートと__init__.pyと__all__の意味

# from lesson_package.talk import human
# from lesson_package.talk import animal

# あまり好まれない
# 上記の2つのモジールをまとめてimportする
from lesson_package.talk import *
# talkフォルダの__init__.pyに__all__ =['human','animal']を追加する

# VSCode上には赤い波線が残るが一応実行できる。 Pycharmでは赤波線が消える
print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())
