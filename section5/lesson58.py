# ラムダ

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# ラムダを使わない
def sample_func(word):
    return word.capitalize()


change_words(l, sample_func)

# ラムダを使う：コード量の削減
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
