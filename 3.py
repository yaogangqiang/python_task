result, a, b = 0, 1, 2
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
while b < 4000000:
    if is_even(b):
        result += b
    a, b = b, a+b

print result
