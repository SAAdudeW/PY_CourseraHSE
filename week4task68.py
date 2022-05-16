def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


a, n = float(input()), int(input())
print(power(a, n))


def FastPow(a, n):
    b = 0
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * FastPow(a, n - 1)
    else:
        if b == 0:
            b = a * a
            k = n / 2
        if k == 0:
            return 1
        return b * FastPow(b, k - 1)


a, n = float(input()), int(input())
print(FastPow(a, n))
