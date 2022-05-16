def IsPrime(n):
    div = i = 1
    while i <= n ** 0.5:
        if n % i == 0 and div == 1:
            div = i
        i = i + 1
    if div == 1:
        return True
    else:
        return False


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
