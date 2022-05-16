a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)

n = int(input())
s = 0
k = 1
while k < n + 1:
    s = s + 1 / (k ** 2)
    k = k + 1
print(s)

from math import floor

a = float(input())
print(a - floor(a))

from math import floor

a = float(input())
b = floor(a)
c = round((a - floor(a)) * 100)
print(b, c)

from math import floor, ceil

a = float(input())
if a - floor(a) < 0.5:
    a = floor(a)
else:
    a = ceil(a)
print(a)

p, x, y = int(input()), int(input()), int(input())
s = (x * 100 + y) * (100 + p)
x = s // 10000
y = s // 100 % 100
print(x, y)

a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())
dx = e * d - f * b
dy = - e * c + f * a
d = a * d - c * b
x = dx / d
y = dy / d
print(x, y)

a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    print(-b / 2 / a)
if D > 0:
    x1 = (-b - D ** 0.5) / 2 / a
    x2 = (-b + D ** 0.5) / 2 / a
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
