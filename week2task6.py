a, b, c = int(input()), int(input()), int(input())
if c >= a and c >= b and a >= b:
    (b, a) = (a, b)
elif b >= a and b >= c and a >= c:
    (c, b) = (b, c)
    (b, a) = (a, b)
elif b >= a and b >= c and c >= a:
    (b, c) = (c, b)
elif a >= b and a >= c and b >= c:
    (c, a) = (a, c)
elif a >= b and a >= c and c >= b:
    (a, b) = (b, a)
    (b, c) = (c, b)
print(a, b, c)
