from util import read_mat, read_vec
A = read_mat()
eps = float(input())
from task_11 import shift_spectrum

sp, Q, good = shift_spectrum(A, eps)
print(sp)
print(Q)
print(good)