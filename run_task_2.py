from util import read_mat, read_vec
A = read_mat()
b = read_vec()
eps = float(input())

from task_2 import gauss_zeidel

print(gauss_zeidel(A, b, eps))