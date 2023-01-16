def compare_permuted_nums(num1,num2):
    return "".join(sorted([i for i in str(num1)])) == "".join(sorted([i for i in str(num2)]))


def problem52():
    NUM = 100000000
    desired_boolean = True
    for i in range(1,NUM):
        desired_boolean = True
        for j in range(2,7):
            if not compare_permuted_nums(i,i*j):
                desired_boolean = False
                break
        if desired_boolean:
            print("the solution is", i)
            break



if __name__=="__main__":
    problem52()