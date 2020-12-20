from util import Mat, Vec, empty_mat
from task_9_10 import tridiag
from task_11 import shift_spectrum

def make_neighbours(x, y, n):
    return [
        ((x + 2*y)%n, y),
        (((x - 2*y)%n + n)%n, y),
        ((x + (2*y + 1))%n, y),
        (((x - (2*y + 1))%n + n)%n, y),
        (x, (y + 2*x)%n),
        (x, ((y - 2*x)%n + n)%n),
        (x, (y + (2*x + 1))%n),
        (x, ((y - (2*x + 1))%n + n)%n)
    ]
def calc_number(p, n):
    x, y = p
    return x*n + y

def build_exp_first(n):
    G = empty_mat(n**2)
    for x in range(n):
        for y in range(n):
            neighbours = [calc_number(p, n) for p in make_neighbours(x, y, n)]
            for p in neighbours:
                G[calc_number((x, y), n)][p] += 1
                G[p][calc_number((x, y), n)] += 1
    return G 

def make_neighbours_second(x, n):
    if (x == 0):
        return [1, n-1, n]
    elif (x == n):
        return [n, n, 0]
    else:
        return [(x + 1)%n, (x - 1 + n)%n, pow(x, n-2, n)]

def build_exp_second(n):
    G = empty_mat(n + 1)
    for x in range(n + 1):
        for y in make_neighbours_second(x, n):
            G[x][y] += 1
            G[y][x] += 1
    return G


#n -- n из первой или p из второй. Для первой передавать build_exp_first, 
# для второй -- build_exp_second

def calc_alpha(n, graph_builder):
    G = graph_builder(n)
    d = (G*Vec([1]*len(G)))[0]
    A, _ = tridiag(G)
    sp, _, good = shift_spectrum(A, 0.00001, 1e5)

    sp.sort(reverse=True)

    l = max(abs(sp[1]), abs(sp[-1]))

    return (l/d, good)