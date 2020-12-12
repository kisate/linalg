from util import *

def gauss(A : Mat, b : Vec):
    n = len(b)
    res = Vec([x for x in b])
    for i in range(n):
        res[i] /= A[i][i]
        for j in range(i+1, n):
            res[j] -= res[i]*A[j][i]

    return res

def gauss_zeidel(A : Mat, b : Vec, eps):
    zeroes = True
    n = len(A)
    L = empty_mat(n)
    U = empty_mat(n)
    for i in range(n):
        zeroes &= A[i][i] == 0
        for j in range(i, n):
            L[j][i] = A[j][i]

    for i in range(n):
        for j in range(0, i):
            U[j][i] = A[j][i]
    
    if zeroes: 
        return 0
    

    x_i = Vec([1/n**0.5]*n)
    iters = 20

    while abs(A*x_i - b) > eps:
        x_ni = gauss(L, b - U*x_i) 
        if abs(x_ni) >= abs(x_i) + 1:
            iters -= 1
        else:
            iters = 20
        if iters < 0:
            return 0
        x_i = x_ni

    return x_i
