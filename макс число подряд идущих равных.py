p = n = int(input())
c = cc = 0

while n != 0:

    if n == p:
        cc += 1
        if cc > c:
            c = cc
    else:
        cc = 1

    p = n
    n = int(input())

print(c)
