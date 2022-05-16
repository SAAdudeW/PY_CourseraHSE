n = int(input())
m = n
am = 0
amm = 0
while n != 0:
    if n == m:
        am = am + 1
    if am > amm:
        amm = am
        if n != m:
            am = 1
    m = n
    n = int(input())
print(amm)
