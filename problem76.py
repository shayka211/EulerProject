import tqdm
import numpy as np
def partitions(n):
    parts = [1]+[0]*n
    for t in range(1, n+1):
        # print(parts)
        for i, x in enumerate(range(t, n+1)):
            parts[x] += parts[i]

    return parts[n]


def problem76():
    # since they want partition of length>1 we will substract 1
    print("the solution is",partitions(100)-1)
    # print("the solution is",partitions_count(1000)-1)






if __name__=="__main__":
    problem76()
