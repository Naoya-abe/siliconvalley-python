# Noneを判定する場合(nullオブジェクト)

is_empty = None
# print(is_empty)

# PythonではNomeの判定で「==」は使わない「is」を使う
if is_empty is None:
    print('None!!!')

# 「==」と「is」の違い
print(1 == True)  # 値が同じか？
print(1 is True)  # オブジェクト同士が同じか？

# 「is」を使うのは、ほぼ「None」のとき
