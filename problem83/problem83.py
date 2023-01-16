from EulerProject.problem81.problem81 import read_txt_file_as_matrix
from EulerProject.problem81.problem81 import sum_of_path
import networkx as nx
import tqdm

def problem_83():
    matrix = read_txt_file_as_matrix(r"C:\Users\USER\Documents\python-algorithmic-stuff\EulerProject\problem82\p082_matrix.txt")
    G = nx.DiGraph()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > 0:
                G.add_edge((i, j), (i - 1, j), weight=matrix[i - 1, j])
            if j > 0:
                G.add_edge((i, j), (i, j - 1), weight=matrix[i, j - 1])
            if j < len(matrix)-1:
                G.add_edge((i, j), (i, j+1), weight=matrix[i, j+1])
            if i < len(matrix)-1:
                G.add_edge((i, j), (i+1, j), weight=matrix[i+1, j])

    shortest_path = nx.dijkstra_path(G, (0, 0), (len(matrix)-1, len(matrix)-1))

    print("solution is ", sum_of_path(G, shortest_path) + matrix[0][0])

if __name__ =="__main__":
    problem_83()