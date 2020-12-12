from util import Mat, Vec, uni_mat
from task_3_4 import giv_qr
from task_5_6 import haus_qr


def simple_spectrum(A: Mat, eps):
    Ai = A
    Q = uni_mat(len(Ai))
    while max([x[1] for x in Ai.hersh_circles()]) >= eps:
        Qi, R = haus_qr(Ai)
        Ai = R*Qi
        Q = Q*Qi
    return ([Ai[i][i] for i in range(len(A))], Q)
    # return (A, Q)