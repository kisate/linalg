from util import Mat, Vec, uni_mat, empty_mat, uni_vec, EPS
from task_5_6 import haus_rotate
from task_3_4 import giv_rotate

def right_haus_rotate(A: Mat, v: Vec):
    return A - (Mat([[x] for x in A*v]))*(Mat([[x for x in v]]))*2

def tridiag(A: Mat):
    n = len(A)
    A = A.copy_mat()
    Q = uni_mat(n)

    for k in range(n-1):
        v = Vec([0]*n)
        for i in range(k+1, n):
            v[i] = A[i][k]
        u = v.normed() - uni_vec(k+1, n)
        if (abs(u) < EPS):
            continue
        A = haus_rotate(A, u.normed())
        A = right_haus_rotate(A, u.normed())
        Q = haus_rotate(Q, u.normed())
    
    return (A, Q.transpose())

def tridiag_qr(A: Mat, extra=[]):
    n = len(A)
    A = A.copy_mat()
    Q = uni_mat(n)

    for i in range(1, n):
        if abs(A[i][i-1]) > EPS:
            c = A[i-1][i-1] / (A[i-1][i-1]**2 + A[i][i-1]**2)**0.5
            s = -A[i][i-1] / (A[i-1][i-1]**2 + A[i][i-1]**2)**0.5
            giv_rotate(A, i, i-1, c, s)
            giv_rotate(Q, i, i-1, c, s)
            for x in extra:
                giv_rotate(x, i, i-1, c, s)
    
    return (Q.transpose(), A)

def tridiag_spectrum(A: Mat, eps, steps=1e9):
    Ai = A
    Q = uni_mat(len(Ai))
    while max([x[1] for x in Ai.hersh_circles()]) >= eps and steps > 0:
        Qi, R = tridiag_qr(Ai)
        Ai = R*Qi
        Q = Q*Qi
        steps -= 1
    return ([Ai[i][i] for i in range(len(A))], Q, steps != 0)