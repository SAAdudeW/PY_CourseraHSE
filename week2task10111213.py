N = int(input())
i = 1
while i ** 2 <= N:
    print(i ** 2, end=' ')
    i = i + 1

n = int(input())
d = i = n
while i > 2:
    i = i - 1
    if n % i == 0:
        d = i
print(d)

X, Y = int(input()), int(input())
n = 1
while X < Y:
    X = X * 1.1
    n = n + 1
print(n)

a = int(input())
m = a
while a != 0:
    if a > m:
        m = a
    a = int(input())
print(m)
