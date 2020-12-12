from typing import List

EPS = 0.0000000001

class Vec:
    def __init__(self, coords : List):
        self.coords = coords
    def __getitem__(self, i):
        return self.coords[i]
    def __setitem__(self, i, x):
        self.coords[i] = x
    def __str__(self):
        return "Vec" + str(self.coords)
    def __repr__(self):
        return "Vec" + repr(self.coords)
    def __len__(self):
        return len(self.coords)
    def __sub__(self, b):
        n = len(self)
        res = [0]*n
        for i in range(n):
            res[i] = self[i] - b[i]
        return Vec(res)
    def __add__(self, b):
        n = len(self)
        res = [0]*n
        for i in range(n):
            res[i] = self[i] + b[i]
        return Vec(res)
    def __abs__(self):
        return sum([abs(x)**2 for x in self])**0.5
    def __mul__(self, b):
        return Vec([x * b for x in self])
    def normed(self):
        return self * (1/abs(self))

class Mat:
    def __init__(self, mat):
        self.mat = [Vec(x) for x in mat]
    def __getitem__(self, i):
        return self.mat[i]
    def __setitem__(self, i, x):
        self.mat[i] = x
    def __str__(self):
        return "Mat\n" + "\n".join(str(x) for x in self.mat)
    def __repr__(self):
        return "Mat\n" + "\n".join(repr(x) for x in self.mat)
    def __len__(self):
        return len(self.mat)
    def __sub__(self, b : 'Mat'):
        n = len(self)
        m = len(self[0])
        res = empty_mat(n, m)
        for i in range(n):
            for j in range(m):
                res[i][j] = self[i][j] - b[i][j]
        return res
    def __add__(self, b : 'Mat'):
        n = len(self)
        m = len(self[0])
        res = empty_mat(n, m)
        for i in range(n):
            for j in range(m):
                res[i][j] = self[i][j] + b[i][j]
        return res
    def __mul__(self, b):
        if type(b) is Vec:
            return multiply_mat_vec(self.mat, b)
        elif type(b) is Mat:
            n = len(self)
            m = len(self[0])
            res = empty_mat(n, len(b[0]))
            for i in range(n):
                for j in range(len(b[0])):
                    for k in range(m):
                        res[i][j] += self[i][k]*b[k][j]
            return res
        elif type(b) is float or type(b) is int:
            return Mat([[b*x for x in y] for y in self])

    def hersh_circles(self):
        n = len(self)
        m = len(self[0])
        circles = []
        for i in range(n):
            c = self[i][i]
            r = 0 
            for j in range(m):
                if i != j:
                    r += abs(self[i][j])
            circles.append((c, r))
        return circles
    
    def copy_mat(self):
        return Mat([
            [x for x in y] for y in self
        ])

    def transpose(self):
        n = len(self)
        m = len(self[0])
        res = empty_mat(m, n)
        for i in range(n):
            for j in range(m):
                res[i][j] = self[j][i]
        return res

    def __abs__(self):
        return sum([abs(x) for x in self])

    def repr_approx(self):
        return "\n".join([" ".join(["{:.2f}".format(x) for x in y]) for y in self])


def multiply_mat_vec(mat, vec):
    n = len(mat)
    m = len(mat[0])
    res = Vec([0]*n)
    for i in range(n):
        for j in range(m):
            res [i] += mat[i][j] * vec[j]
    return res

def uni_mat(n, c=1):
    res = []
    for i in range(n):
        res.append([0]*n)
        res[i][i] = c
    return Mat(res)

def uni_vec(i, n):
    res = Vec([0]*n)
    res[i] = 1
    return res

def empty_mat(n, m=None):
    res = []
    if (m is None):
        m = n
    for _ in range(n):
        res.append([0]*m)
    return Mat(res)

def vec_norm(vec):
    return sum([abs(x)**2 for x in vec])**0.5