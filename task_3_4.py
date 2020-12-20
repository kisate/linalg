from util import Vec, Mat, EPS, uni_mat, read_mat, read_vec

def giv_rotate(A : Mat, i, j, c, s):
    if (abs(s**2 + c**2 - 1) > EPS):
        raise "s^2 + c^2 != 1"


    u = A[i]*c + A[j]*s
    v = A[i]*(-s) + A[j]*c

    A[i] = u
    A[j] = v

def giv_qr(A : Mat):
    n = len(A)
    A = A.copy_mat()
    Q = uni_mat(n)

    for i in range(n):
        k = i
        while k < n and abs(A[k][i]) <= EPS :
            k += 1
        
        for j in range(k + 1, n):
            if (abs(A[j][i]) > EPS):
                c = A[k][i] / (A[k][i]**2 + A[j][i]**2)**0.5
                s = -A[j][i] / (A[k][i]**2 + A[j][i]**2)**0.5
                giv_rotate(A, j, k, c, s)
                giv_rotate(Q, j, k, c, s)
        if k < n and abs(A[i][i]) <= EPS:
            giv_rotate(A, i, k, 0, 1)
            giv_rotate(Q, i, k, 0, 1)
    
    return (Q.transpose(), A)
