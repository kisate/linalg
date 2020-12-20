from util import read_mat, read_vec
A = read_mat()
i = int(input())
j = int(input())
c = int(input())
s = int(input())

from task_3_4 import giv_rotate

giv_rotate(A, i, j, c, s)

print(A)