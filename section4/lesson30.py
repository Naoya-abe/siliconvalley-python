# 集合の使い所
# 共通点を探す時に使える

# 例：SNSで自分と友達の共通の友人を探す
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
print('#####################')

# ECサイトで購入したものの種類を取得
f = ['apple', 'apple', 'banana', 'banana']
kind = set(f)  # 集合型に型変換
print(kind)
