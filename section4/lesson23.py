# タプルの使い所
# 選択肢が3つある質問をユーザに投げて、その中から2つ選んでもらう

# OK 質問のところを書き換えできないようにする
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

# chose_from_two.append('A')　タプルで書けばここはエラーが出るのでバグがすぐわかる
# chose_from_two.append('C')

print(chose_from_two)
print(answer)

print('##############################')

# NG
chose_from_two_ng = ['A', 'B', 'C']

answer = []
chose_from_two_ng.append('A')
chose_from_two_ng.append('C')
print(chose_from_two)
print(answer)
