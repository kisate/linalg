from util import read_mat, read_vec
A = read_mat()
x_0 = read_vec()
eps = float(input())
from task_7 import simple_iter

print(simple_iter(A, x_0, eps))
