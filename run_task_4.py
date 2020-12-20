from util import read_mat, read_vec
A = read_mat()
from task_3_4 import giv_qr

q, r = giv_qr(A)
print(q)
print(r)