from scipy.special import binom
if __name__ =="__main__":
    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if i >= j and binom(i, j) > 1000000:
                count += 1
    print("the solution is", count)
