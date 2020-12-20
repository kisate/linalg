from util import read_mat, read_vec
A = read_mat()
b = read_vec()
eps = float(input())

from task_1 import simple_it

print(simple_it(A, b, eps))