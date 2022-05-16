n = int(input())
m = n
am = 0
while n != 0:
    if n >= m:
        am = am + 1
        m = n
    n = int(input())
    if n > m:
        am = 0
print(am)
