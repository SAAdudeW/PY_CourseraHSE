n = int(input())
m = n
mm = 0
while n != 0:
    if mm < n < m:
        mm = n
    if n > m:
        mm = m
        m = n
    n = int(input())
print(mm)
