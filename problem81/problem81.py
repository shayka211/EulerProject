import numpy as np
import networkx as nx
import pandas as pd
import itertools


def read_txt_file_as_matrix(url):
    arr2d = []
    with open(url) as file:
        for line in file:
            list_from_string = line.rstrip('\n').split(",")
            list_of_integers = [int(num) for num in list_from_string]
            arr2d.append(list_of_integers)
    return np.array(arr2d)


def problem_81():
    matrix = read_txt_file_as_matrix(r"C:\Users\USER\Documents\python-algorithmic-stuff\EulerProject\problem81\p081_matrix.txt")
    print(pd.DataFrame(matrix))
    G = nx.DiGraph()
    # vertices = list(itertools.combinations([i for i in range(len(matrix))], 2))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j < len(matrix)-1:
                G.add_edge((i, j), (i, j+1), weight=matrix[i, j+1])
            if i < len(matrix)-1:
                G.add_edge((i, j), (i+1, j), weight=matrix[i+1, j])
    shortest_path = nx.dijkstra_path(G, (0, 0), (len(matrix)-1, len(matrix)-1))
    print(shortest_path)
    print("solution is ", sum_of_path(G, shortest_path) + matrix[0, 0])



def sum_of_path(G, path):
    sum = 0
    for i in range(len(path)-1):
        sum += G[path[i]][path[i+1]]['weight']
    return sum

    # print(list(G.nodes))
    # print(list(G.edges))

if __name__ =="__main__":
    problem_81()









