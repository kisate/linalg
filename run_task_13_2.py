from util import read_mat, read_vec
n = int(input())
from task_13 import build_exp_second, calc_alpha

print(calc_alpha(n, build_exp_second))