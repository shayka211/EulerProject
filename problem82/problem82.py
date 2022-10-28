from EulerProject.problem81.problem81 import read_txt_file_as_matrix
import pandas as pd
import networkx as nx
import tqdm

def problem_82():
    matrix = read_txt_file_as_matrix(r"C:\Users\USER\Documents\python-algorithmic-stuff\EulerProject\problem82\p082_matrix.txt")
    # print(pd.DataFrame(matrix))
    G = nx.DiGraph()
    # vertices = list(itertools.combinations([i for i in range(len(matrix))], 2))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > 0:
                G.add_edge((i, j), (i - 1, j), weight=matrix[i - 1, j])
            if j < len(matrix)-1:
                G.add_edge((i, j), (i, j+1), weight=matrix[i, j+1])
            if i < len(matrix)-1:
                G.add_edge((i, j), (i+1, j), weight=matrix[i+1, j])
    arr = []
    for row in tqdm.tqdm(range(len(matrix))):
        for row_end in range(len(matrix)):
            shortest_path = nx.dijkstra_path(G, (row, 0), (row_end, len(matrix)-1))
            arr.append(sum_of_path(G, shortest_path) + matrix[row, 0])

    print("solution is ", min(arr))



def sum_of_path(G, path):
    sum = 0
    for i in range(len(path)-1):
        sum += G[path[i]][path[i+1]]['weight']
    return sum

if __name__ =="__main__":
    problem_82()