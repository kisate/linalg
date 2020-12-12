from util import Mat, Vec, uni_mat, empty_mat, uni_vec, EPS

def haus_rotate(A: Mat, v: Vec):
    return A - (Mat([[x*2] for x in v]))*(Mat([[x for x in v]])*A)

def haus_qr(A:Mat):
    n = len(A)
    A = A.copy_mat()
    Q = uni_mat(n)
    for s in range(n):
        v = Vec([0]*n)
        for i in range(s, n):
            v[i] = A[i][s]
        if (abs(v) < EPS):
            continue
        u = v*(1/abs(v)) - uni_vec(s, n)
        if (abs(u) < EPS): 
            continue
        A = haus_rotate(A, u.normed())
        Q = haus_rotate(Q, u.normed())
    return (Q.transpose(), A)
    