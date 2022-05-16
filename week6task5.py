def CountSort(A):
    a = [0] * 101
    for n in A:
        a[n] += 1
    for n in range(101):
        print((str(n) + ' ') * a[n], end='')


A = map(int, input().split())
CountSort(A)
