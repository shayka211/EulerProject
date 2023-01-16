import useful_functions
import tqdm
import numpy as np
print(useful_functions.all_primes_under_N(100))

OUR_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
SIZE = 10000000

def sol():
    starting_point = 10**12
    values = []
    for i in tqdm.tqdm(range(starting_point, starting_point + SIZE)):
        values.append(hash(tuple([(((i % prime) *((i-1) % prime)) % prime) for prime in OUR_PRIMES])))

    # now we have list of all possible solutions
    # given new solution we want to whether we already found it
    values = np.array(values)
    for i in tqdm.tqdm(range(starting_point, starting_point + SIZE)):
        hashed_possible_option = hash(tuple([((((2*i) % prime) *((i-1) % prime)) % prime) for prime in OUR_PRIMES]))
        a = np.searchsorted(values, hashed_possible_option)
        if a < len(values):
            if values[a] == hashed_possible_option:
                return a
    print("damns me")

print(sol())

