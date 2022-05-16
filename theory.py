class ComplexError(BaseException):
    def __init__(self, Complex, other):
        self.arg1 = Complex
        self.arg2 = other


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep

    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)

    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        else:
            raise ComplexError(self, other)
        return Complex(newRe, newIm)

    __rmul__ = __mul__


class Point(Complex):
    def length(self):
        return (self.re ** 2 + self.im ** 2) ** (1 / 2)

    def __str__(self):
        return str((self.re, self.im))


a1 = Complex(1, 2)
try:
    res1 = a1 * 'abcd'
    print(res1)
except ComplexError as ce:
    print('Error in mul with args:', ce.arg1, ce.arg2)

a2 = Point(3, 4)
a3 = Complex(1, 2)
print(a2.length())
res2 = a1 + a2
print(res2)

a4 = Point(3, 4)
print(a4)
