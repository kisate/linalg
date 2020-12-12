from util import Mat, Vec, uni_mat, EPS, empty_mat
from task_9_10 import tridiag_qr, tridiag_spectrum

def tri_mult(A: Mat, B: Mat):
    n = len(A)
    res = empty_mat(n)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(i, min(i+3, n)):
                res[i][j] += A[i][k]*B[k][j]
    return res


#Решение

def shift_spectrum(A: Mat, eps, steps=1e9):
    Ai = A
    Q = uni_mat(len(Ai))
    n = len(A)
    for i in range(n-1, 0, -1):
        it_steps = steps
        while abs(Vec([Ai[i][j] for j in range(i)])) + abs(Vec([Ai[j][i] for j in range(i)])) >= eps and it_steps > 0:
            M = Mat([
                [A[i-1][i-1], A[i-1][i]],
                [A[i][i-1], A[i][i]]
            ])
            M_sp, _, _= tridiag_spectrum(M, eps, 10)
            s = min(M_sp)
            es = uni_mat(n, s)
            for j in range(i+1, n):
                es[j][j] = 0
            Qt = Q.transpose()
            Qi, R = tridiag_qr(Ai-es, [Qt])
            Ai = R*Qi + es
            Q = Qt.transpose()
            it_steps -= 1

        if it_steps == 0:
            return (None, None)

    return ([Ai[i][i] for i in range(len(A))], Q)
    # return (Ai, Q)