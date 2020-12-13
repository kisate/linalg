from task_11 import shift_spectrum
from task_9_10 import tridiag
from util import Vec, Mat, EPS


#Решение

def check_isometry(A: Mat, B: Mat):
    eps = 0.0001
    steps = 1000

    AT,_  = tridiag(A)
    BT,_  = tridiag(B)

    sa, _, good1 = shift_spectrum(AT, eps, steps)
    sb, _, good2 = shift_spectrum(BT, eps, steps)
    if not (good1 and good2):
        return 1
    if abs(Vec(sa)-Vec(sb)) > eps:
        return 0
    return 1


