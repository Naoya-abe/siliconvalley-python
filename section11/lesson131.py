# optparse
# import sys

# # terminalで入力した文字列を取得できる
# print(sys.argv)

# さらに高機能なoptparse
# https://docs.python.org/ja/3/library/optparse.html#the-store-action

from optparse import OptionParser
from optparse import OptionGroup


def main():
    # terminalからのコマンドの入力の仕方を記述
    useage = 'useage: %prog [options] arg1 arg2'
    # parserの作成
    parser = OptionParser(usage=useage)
    # ファイル名を渡したい  (オプションコマンド、アクション、型、保存先、ヘルプ)
    # action='store'を指定することで、残りの引数から、正しい型を確かめ、指定した保存先（変数：dest）に保存するようoptparseに指示する。
    parser.add_option('-f', '--file', action='store',
                      type='string', dest='filename', help='File name')

    parser.add_option('-n', '--number', action='store', type='int', dest='num')

    # defaultの指定（destが共有されている際）
    parser.set_defaults(verbose=True)
    # 「python lesson131.py -v」で保存先変数にTrueを加える。 defaultはpython lesson131.pyを実行した時にverboseにFalseを代入する
    parser.add_option('-v', action='store_true', dest='verbose')
    # 同じdestを示すことも可能
    parser.add_option('-q', action='store_false', dest='verbose')

    # constで指定した文字列をdestに代入する
    parser.add_option('-r', action='store_const',
                      const='root', dest='user_name')

    # callback
    parser.add_option('-e', dest='env')

    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't release")

    parser.add_option('--release', action='callback',
                      callback=is_release, dest='release')

    # 上記のoptionとはカテゴリ分けをしてoptionを作成したい場合
    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    # 実際にparserを実行する（tupleのアンパッキングを利用）
    options, args = parser.parse_args()
    # dict型で取得
    print(options)
    # ファイル名を取得
    print(options.filename)
    # ファイル名以降の入力値を取得
    print(args)


if __name__ == '__main__':
    main()
