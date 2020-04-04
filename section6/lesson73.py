# 組み込み関数
# url:https://docs.python.org/ja/3/library/functions.html

import builtins

# '__builtins__'の中に組み込み関数が含まれている
print(globals())

print(builtins)


# このリストを点数順に並び替える
ranking = {'a': 100, 'b': 85, 'c': 95}

# 駄目
print(sorted(ranking))

# OK 小さい順
print(sorted(ranking, key=ranking.get))

# OK 大きい順
print(sorted(ranking, key=ranking.get, reverse=True))
