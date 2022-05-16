from sys import stdin
from copy import deepcopy


class Matrix:

    def __init__(self, lliisstt):
        self.listf = deepcopy(lliisstt)

    def __str__(self):
        strform = ''
        for raw in self.listf:
            string = '\t'.join(map(str, raw))
            strform += string
            strform += '\n'
        return strform[:-1]

    def size(self):
        return (len(self.listf), len(self.listf[0]))

    def __add__(self, other):
        sumlist = deepcopy(self.listf)
        summ = Matrix(sumlist)
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                summ.listf[i][j] = summ.listf[i][j] + other.listf[i][j]
        return summ

    def __mul__(self, other):
        mullist = deepcopy(self.listf)
        mulm = Matrix(mullist)
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                mulm.listf[i][j] = mulm.listf[i][j] * other
        return mulm

    __rmul__ = __mul__


exec(stdin.read())
