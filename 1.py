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
