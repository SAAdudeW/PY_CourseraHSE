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


exec(stdin.read())
