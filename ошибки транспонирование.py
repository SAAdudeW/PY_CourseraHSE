from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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

        if self.size()[0] != other.size()[0] \
                or self.size()[1] != other.size()[1]:
            raise MatrixError(self, other)

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

    def transpose(self):
        translist = deepcopy(self.listf)
        jj = []
        for i in range(self.size()[1]):
            ii = []
            for j in range(self.size()[0]):
                ii.append(translist[j][i])
            jj.append(ii)
        self.listf = jj
        return self

    @staticmethod
    def transposed(other):
        translist = deepcopy(other.listf)
        transposed = Matrix(translist)
        jj = []
        for i in range(other.size()[1]):
            ii = []
            for j in range(other.size()[0]):
                ii.append(translist[j][i])
            jj.append(ii)
        transposed.listf = jj
        return transposed


exec(stdin.read())
