from util import read_mat, read_vec
A = read_mat()
eps = float(input())
from task_9_10 import tridiag_spectrum

sp, Q, good = tridiag_spectrum(A, eps)
print(sp)
print(Q)
print(good)