def NOD(x, y):
    if x > y:
        p = y
        while p != 0:
            pr = p
            q = x // y
            p = x - y * q
            x = y
            y = p
    else:
        p = x
        while p != 0:
            pr = p
            q = y // x
            p = y - x * q
            y = x
            x = p
    return pr


def ReduceFraction(n, m):
    p, q = n, m
    while NOD(p, q) != 1:
        d = NOD(p, q)
        p = p // d
        q = q // d
    return (p, q)


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
