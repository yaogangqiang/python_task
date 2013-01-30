# coding=utf-8
# 7x6路径问题
from itertools import combinations

result = []
for i in combinations(range(13), 6):
    result.append(i)

print len(result)
