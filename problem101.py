# ok so assume we have some series and we need to find some polynomial
# a1,a2, a1=1,a2=8,f(1)=a_1,f(2)=a_2,f(x)=ax^2+bx+c, x^2+679x-679
# f(x)=1,f(x)=x+b, f(1)=1
import math
import numpy as np


def un(n):
    return sum([((-1)**i)*(n**i) for i in range(11)])

# a_1=1 f(x)=1
# a1,a2,f(1)=a1,f(2)=a2,f(x)=x^3+ax^2+cx+b
# first_polynomial= 1

def find_ith_approximate_polynomial(i):
    A = np.array([[j**(i-k) for k in range(1,i+1)] for j in range(1,i+1)])
    # print(A)
    b = np.array([un(j) for j in range(1,i+1)])
    x = np.linalg.solve(A, b)
    # print([int(i) for i in x])
    return x


def sub_in_poly(x, k):
    return sum([k**(len(x)-i-1)*x[i] for i in range(len(x))])


def sol():
    sum=0
    for i in range(1,11):
        a=sub_in_poly(find_ith_approximate_polynomial(i), i+1)
        # print("sub in poly ",i,"=", a)
        sum += a

    return sum


# print("first 10 elements",[un(i) for i in range(1,10)])
# print("the 1th approxiamte pol is =",find_ith_approximate_polynomial(2))
print("sum of FITs for the BOPs", sol())