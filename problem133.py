# the idea will be of the following, first try eliminate primes by going over the repunit numbers
# and delete it primes
import tqdm

import useful_functions
import sympy
import numpy as np
from sympy.ntheory import factorint
# not finished



def problem133():
    all_primes_under_100000 = np.array(useful_functions.all_primes_under_N(100000))
    all_relevant_primes = all_primes_under_100000
    print(len(all_relevant_primes))
    for i in tqdm.tqdm(range(1, 34)):
        num = int("".join([str(1) for j in range(10**i)]))
        repunit_num = int("".join([str(1) for j in range(i)]))
        all_relevant_primes = delete_sub_list_from_list(prime_factorization(repunit_num),all_relevant_primes)
    return all_relevant_primes



def delete_sub_list_from_list(sub_list, lis):
    temp_lis = lis
    for item in sub_list:
        temp_lis = np.delete(temp_lis, np.where(temp_lis == item))
    return temp_lis


def prime_factorization(num):
    return factorint(num).keys()


def prime_divides_some_repunit_num(p):
    optional_num = ''
    count = 0
    while count < 10000:
        count = count + 1
        for i in range(10):
            temp = p * int(str(i) + optional_num)
            bool = temp % (10 ** count) == int("".join([str(1) for j in range(count)]))
            if bool:
                optional_num = str(i) + str(optional_num)
                # print(optional_num)
                # print(p*int(optional_num))
                break
        # print(count)
        if is_rep_unit_num(int(optional_num) * p) and is_a_power_of_10(str(int(optional_num) * p)):
            return True
        elif not is_a_power_of_10(str(int(optional_num) * p)):
            print(len(str(int(optional_num) * p)))
    return False


def is_rep_unit_num(num):
    return '1' == ''.join(set(str(num)))
def is_a_power_of_10(num):
    return '10' == ''.join(set(str(num))) or '01' == ''.join(set(str(num)))

# print(prime_divides_some_repunit_num(11))
# print(prime_divides_some_repunit_num(17))
# print(prime_divides_some_repunit_num(11))
# print(prime_divides_some_repunit_num(73))
# print(prime_divides_some_repunit_num(19))
problem133()