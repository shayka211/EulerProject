# minimum spanning tree is easy

import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

af = open('p107_network.txt')
matrix = []
for line in af:
    new_line = []
    for v in line.strip().split(','):
        if v == '-':
            new_line.append(0)
        else:
            new_line.append(int(v))
    matrix.append(new_line)

X = csr_matrix(matrix)
old_sum = sum([sum(line) for line in matrix]) / 2
mst = minimum_spanning_tree(X)
new_sum = sum([sum(line) for line in mst.toarray()])
print(old_sum - new_sum)
