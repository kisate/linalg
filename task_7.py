from util import Vec, Mat, uni_mat, uni_vec, empty_mat

def calc_form(A: Mat, v: Vec):
    return (Mat([[x for x in v]])*(A*v))[0]

def simple_iter(A: Mat, x_0: Vec, eps):
    steps = 100000
    x_i = x_0
    while steps > 0 and abs(A*x_i - x_i*calc_form(A, x_i)) > eps:
        x_i = (A*x_i).normed()
        steps -= 1
    
    if steps == 0:
        return 0
    
    return (x_i, calc_form(A, x_i))