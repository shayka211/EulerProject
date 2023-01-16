import numpy as np

SIZE = 2 ** 30
CHUNK_SIZE = 10000


def is_bouncy(num):
    if len(str(num)) < 3:
        return False
    if all(int(str(num)[i]) <= int(str(num)[i + 1]) for i in range(len(str(num)) - 1)):
        return False
    if all(int(str(num)[i]) >= int(str(num)[i + 1]) for i in range(len(str(num)) - 1)):
        return False
    return True


def proportion_between_list_of_ones_and_zeros(my_list: np.array):
    return np.count_nonzero(my_list) / len(my_list)


def sol(threshold):
    number_of_bouncy_numbers_so_far = 0
    for i in range(1, SIZE):
        if is_bouncy(i):
            number_of_bouncy_numbers_so_far += 1
        if number_of_bouncy_numbers_so_far / i >= threshold and number_of_bouncy_numbers_so_far / (i+1) < threshold:
            return i


print("the solution is", sol(0.99))
