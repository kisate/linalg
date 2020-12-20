from util import read_mat, read_vec
A = read_mat()
eps = float(input())
from task_8 import simple_spectrum

sp, Q, good = simple_spectrum(A, eps)
print(sp)
print(Q)
print(good)