# coding=utf-8
# Pandigital products


def is_pandigital(*args):
    num = sorted(''.join(str(arg) for arg in args))
    length = 9
    if len(num) != length:
        return False

    for i in range(len(num)):
        if str(i + 1) != str(num[i]):
            return False
    return True


def main():
    pandigitals = set()
    total = 0
    for multiplicand in range(100, 5000):
        for multiplier in range(1, 100):
            product = multiplicand * multiplier
            if is_pandigital(multiplicand, multiplier, product):
                pandigitals.add(product)
    print sum(pandigitals)

if __name__ == "__main__":
    main()
