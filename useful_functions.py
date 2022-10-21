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
