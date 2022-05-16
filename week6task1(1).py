def merge(x, y):
    c = x + y
    j = k = 0
    for i in range(len(x) + len(y)):
        if j < len(x):
            if k < len(y):
                if x[j] < y[k]:
                    c[i] = x[j]
                    j = j + 1
                else:
                    c[i] = y[k]
                    k = k + 1
            else:
                c[i] = x[j]
                j = j + 1
        else:
            c[i] = y[k]
            k = k + 1
    return c


A, B = list(map(int, input().split())), list(map(int, input().split()))
print(' '.join(map(str, merge(A, B))))
