# セミコロンは要らない
x = 1
y = 2

# １行は80文字以内
x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# 変数が長くなりそうなときは2行にする


def test_func(x, y, z,
              foperfjesoigntdrhoydjthktypgaejrpesotgmprsdmponbkf='test'):
    """
    :param x:
    :param y:
    :param z:
    :param foperfjesoigntdrhoydjthktypgaejrpesotgmprsdmponbkf:
    :return:

    URLは長くても1行で書いたほうが良い
    See details at:http://naoyaabe.com/fijorwafubesgittorujgipeagjjjjjjrrrrrrrrrrrrrrrepoagrkdot
    """


# 条件が一つの場合は無駄な()を書かない
# if (x and y):
if x and y:
    print('exists')

    # インデントは4つ！
    x = {'test': 'sss'}

# 代入は = の両端にスペースを入れる *関数宣言の引数はスペースいらない
x = y

# わかりやすいstrの書き方
word = 'hello'
word2 = '!'

# bad
new_word = '{}{}'.format(word, word2)
# good
new_word = word + word2

# forループで長い文字列を生成する際

# bad
long_word = ""
for word in ['fmwaempr', 'fmaopgmeprs', 'fmafmeosp']:
    long_word += "{}fwejaifoera".format(word)

# good メモリの使用量が少ない
long_word = []
for word in ['fmwaempr', 'fmaopgmeprs', 'fmafmeosp']:
    long_word.append("{}fjeior".format(word))
new_long_word = ''.join(long_word)


# 文字列 ''と""は会社のルールに合わせる
print('frmwaforp')
print("fwakofker")

# if文は2行
if x:
    print('exit')
else:
    print('else')
