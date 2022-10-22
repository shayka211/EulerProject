def row_separated_by_commas_to_list(my_str):
    return my_str.split(",")


def get_list_of_sets_from_text_separated_by_commas(url):
    all_sets = []
    with open(url) as f:
        for line in f.readlines():
            my_str = row_separated_by_commas_to_list(line)
            float_list = [float(i) for i in my_str]
            all_sets.append(float_list)
    return all_sets



def all_primes_under_N(max_n):
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))