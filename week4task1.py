def min4(a, b, c, d):
    q = min(a, b)
    w = min(q, c)
    e = min(w, d)
    return e


x, y, z, v = int(input()), int(input()), int(input()), int(input())
print(min4(x, y, z, v))
