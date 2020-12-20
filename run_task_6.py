from util import read_mat, read_vec
A = read_mat()
from task_5_6 import haus_qr

q, r = haus_qr(A)
print(q)
print(r)