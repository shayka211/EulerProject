import functools
from useful_functions import all_primes_under_N
from problem76 import partitions
def partitions():
    target = 1
    while True:
        parts = [1]+[0]*target
        for t in all_primes_under_N(1000):
            # print(parts)
            for i, x in enumerate(range(t, target+1)):
                parts[x] += parts[i]
        if parts[target] > 5000:
            break
        target +=1
    return target


if __name__ == "__main__":
    print(partitions())


    # Outputs:
    # sum([3, 8, 4])=15
    # sum([3, 5, 7])=15
    # sum([8, 7])=15
    # sum([5, 10])=15