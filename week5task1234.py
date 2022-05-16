a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(i)

a, b = int(input()), int(input())
if a <= b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

n = int(input())
for i in range(1, n + 1):
    print('+___', end=' ')
print()
for i in range(1, n + 1):
    print('|', end='')
    print(i, end=' ')
    print('/ ', end='')
print()
for i in range(1, n + 1):
    print('|__\\', end=' ')
print()
for i in range(1, n + 1):
    print('|   ', end=' ')

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
