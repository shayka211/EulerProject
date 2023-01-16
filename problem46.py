# so we are looking for all the numbers of the form
#  prime + 2*square of integer
# assume we want to get all possible options, then prime + 2*square<n \to  square<(n - prime)/2
import numpy as np
import useful_functions
import tqdm
SIZE = 2**20


def sol():
    generate_possible_odd_numbers = np.ones(SIZE)
    for i in range(len(generate_possible_odd_numbers)):
        if i % 2 == 0:
            generate_possible_odd_numbers[i] = 0

    all_primes = useful_functions.all_primes_under_N(SIZE)
    for prime in tqdm.tqdm(all_primes):
        for num in range(round(np.sqrt((SIZE - prime)/2) + 2)):
            if prime + 2 * num ** 2 < SIZE:
                generate_possible_odd_numbers[prime + 2*num**2] = 0
    return np.where(generate_possible_odd_numbers == 1)

print(sol())
