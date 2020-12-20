from util import read_mat, read_vec
A = read_mat()
from task_9_10 import tridiag_qr

R, Q = tridiag_qr(A)
print(R)
print(Q)