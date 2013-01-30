def p(number_list, n):
    if n == 0:
        yield []
    else:
        for i in range(len(number_list)):
            for temp_list in p(number_list, n - 1):
                if not number_list[i] in temp_list:
                    yield [number_list[i]] + temp_list


def c(number_list, n):
    n = len(number_list)
    for temp_list in p(range(n), n):
        if sorted(temp_list) == list(temp_list):
            yield [number for number in temp_list]
