from util import read_mat, read_vec
A = read_mat()
B = read_mat()
from task_12 import check_isometry

print(check_isometry(A, B))