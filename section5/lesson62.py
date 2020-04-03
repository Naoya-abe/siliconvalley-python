# 集合内包表記

s = set()

for i in range(10):
    s.add(i)

print(s)

g = {i for i in range(10) if i % 2 == 0}
print(g)
