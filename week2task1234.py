A = int(input())
B = int(input())
max = A
if B > A:
    max = B
print(max)

A = int(input())
B = int(input())
if A > B:
    print('1')
elif B > A:
    print('2')
else:
    print('0')

A = int(input())
B = int(input())
C = int(input())
if A >= B and A >= C:
    max = A
elif B >= A and B >= C:
    max = B
else:
    max = C
print(max)

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')
