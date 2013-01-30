# coding=utf-8
#编写两个函数，p(l, n) 和 c(l, m)，分别求出列表元素的排列和组合
from itertools import permutations
from itertools import combinations


def p(mylist, number):
    result = []
    for i in permutations(mylist, number):
        result.append(list(i))
    print result


def c(mylist, number):
    result = []
    for i in combinations(mylist, number):
        result.append(list(i))
    print result

if __name__ == "__main__":
    p(range(3), 3)
    p(range(3), 2)
