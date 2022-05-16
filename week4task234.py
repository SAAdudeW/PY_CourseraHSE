def IsPointInSquare(a, b):
    return -1 <= a <= 1 and -1 <= b <= 1


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


x, y, xc, yc, r = float(input()), float(input()), \
                  float(input()), float(input()), float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')


    def MinDivisor(n):
        div = i = 1
        while i < n ** 0.5 + 1:
            if n % i == 0 and div == 1:
                div = i
            i = i + 1
        if div == 1:
            return n
        else:
            return div


    n = int(input())
    print(MinDivisor(n))
