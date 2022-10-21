from math import sqrt

def isPandigital(s):
    return set(s) == set('123456789')

rt5=sqrt(5)
def mypow(x, n):
    res = 1.0
    for i in range(n):
        res *= x
        # truncation to avoid overflow:
        if res > 1E20: res *= 1E-10
    return res


def check_first_digits(n):
    # this is an approximation for large n:
    F = mypow( (1+rt5)/2, n )/rt5
    s = '%f' % F
    if isPandigital(s[:9]):
        print(n)
        return True

a, b, n = 1, 1, 1
while True:
    if isPandigital(str(a)[-9:]):
        # print(a)
        # Only when last digits are
        # pandigital check the first digits:
        if check_first_digits(n):
            break
    a, b = b, a+b
    b = b%1000000000
    n += 1

print(n)