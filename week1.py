name = input()
print('Hello, ', name, '!', sep='')

n = int(input())
pengiun = '   _~_    '
print(pengiun * n)
pengiun = '  (o o)   '
print(pengiun * n)
pengiun = ' /  V  \  '
print(pengiun * n)
pengiun = '/(  _  )\ '
print(pengiun * n)
pengiun = '  ^^ ^^   '
print(pengiun * n)

K = int(input())
N = int(input())
print(N // K)

K = int(input())
N = int(input())
print(N % K)

N = int(input())
print(2 ** N)

N = int(input())
print(N % 10)

N = int(input())
print(N // 10)

N = int(input())
print(N % 10 + (N // 10) % 10 + N // 100)

print('A' * 100)

N = int(input())
print(N % (24 * 60) // 60, N % (24 * 60) % 60)

A = int(input())
B = int(input())
N = int(input())
C = A * 100 + B
print(C * N // 100, C * N % 100)

N = int(input())
print('The next number for the number ', N, ' is ', N + 1, '.', sep='')
print('The previous number for the number ', N, ' is ', N - 1, '.', sep='')
