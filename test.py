from task_1 import simple_it
from task_2 import gauss, gauss_zeidel
from task_3_4 import giv_qr
from task_5_6 import haus_rotate, haus_qr
from task_7 import simple_iter
from task_8 import simple_spectrum
from task_9_10 import tridiag, tridiag_qr, tridiag_spectrum
from task_12 import check_isometry
from task_11 import shift_spectrum
from task_13 import build_exp_first, build_exp_second, calc_alpha
from util import Mat, Vec, uni_mat, EPS, empty_mat
import numpy as np
A = [
    [1, 1, -3, 1],
    [-5, 3, -4, 1],
    [1, 3, 2, 0],
    [1, 0, 0, 2]
] 

B = [
    [1,2,3,4],
    [4,3,2,1],
    [8,6,3,1],
    [9,4,1,5]
]

AA = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


AB = [
    [1,2,3],
    [2,5,6],
    [3,6,9]
]

AC = [
    [1,2,3,4,5,6,7],
    [2,6,7,8,8,9,1],
    [3,7,0,1,3,4,5],
    [4,8,1,2,8,6,5],
    [5,8,3,8,3,1,5],
    [6,9,4,6,1,4,9],
    [7,1,5,5,5,9,5],
]

AD = [
    [1,2,0,0,0,0],
    [2,4,5,0,0,0],
    [0,5,0,9,0,0],
    [0,0,9,7,2,0],
    [0,0,0,2,8,3],
    [0,0,0,0,3,4],

]


G1 = [
    [0,1,1,0,0],
    [1,0,1,0,1],
    [1,1,0,0,0],
    [0,0,0,0,1],
    [0,1,0,1,0]
]

G2 = [
    [0,1,1,0,1],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,0,0,1,0]
]

# TEST_N = 50

# TEST_MAT = empty_mat(TEST_N)
# import random
# for i in range(TEST_N):
#     for j in range(i, TEST_N):
#         x = random.randint(0, 10)
#         TEST_MAT[i][j] = x
#         TEST_MAT[j][i] = x
# v, w = np.linalg.eig(np.array(TEST_MAT))
# print(TEST_MAT)
# TD, Q = tridiag(TEST_MAT)
# sp, Q, good = shift_spectrum(TD, 0.00001)

# print(sorted(sp))
# print(sorted(v))
# print(abs(Vec(sorted(sp)) - Vec(sorted(v))))
# print(good)

# MAT_2 = [
#     [0,1,1,0,0,0],
#     [1,0,0,1,0,0],
#     [1,0,0,0,1,0],
#     [0,1,0,0,0,1],
#     [0,0,1,0,1,0],
#     [0,0,0,1,0,0]
# ]

# TD, Q = tridiag(Mat(MAT_2))
# print(TD)
# sp, Q, good = shift_spectrum(TD, 0.00001)
# v, w = np.linalg.eig(np.array(MAT_2))

# print(good)
# print(sorted(sp))
# print(sorted(v))


# v = Vec([1+1j, 2, 3j, -1j])
# print(simple_iter(Mat(A), v, 0.00001))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

for i in primes:
    print(i)
    print(calc_alpha(i, build_exp_second))