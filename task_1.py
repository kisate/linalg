from util import *

def check_circle(circle):
    return abs(circle[0]) + abs(circle[1]) < 1

def simple_it(A : Mat, b: Vec, eps):
    n = len(A)
    e_n = uni_mat(n)
    A = e_n - A
    x_i = Vec([1]*n)
    iters = 20
    h = not all([check_circle(x) for x in A.hersh_circles()])
    while abs(x_i - A*x_i - b) > eps:
        x_ni = A*x_i + b
        if abs(x_ni) >= abs(x_i) + 1:
            iters -= 1
        else:
            iters = 20
        if iters < 0 and h:
            return 0
        x_i = x_ni
    return x_i
