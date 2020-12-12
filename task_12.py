from task_11 import shift_spectrum
from task_9_10 import tridiag
from util import Vec, Mat, EPS

def check_isometry(A: Mat, B: Mat):
    eps = 0.0001
    steps = 1000

    AT,_  = tridiag(A)
    BT,_  = tridiag(B)

    sa, _ = shift_spectrum(AT, eps, steps)
    sb, _ = shift_spectrum(BT, eps, steps)
    if sa is None or sb is None:
        return 1
    if abs(Vec(sa)-Vec(sb)) > eps:
        return 0
    return 1


