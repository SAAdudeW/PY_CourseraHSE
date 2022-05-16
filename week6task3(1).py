n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    xx = (x[i], i + 1)
    x[i] = xx
x.sort()

m = int(input())
y = list(map(int, input().split()))
i = 0
for i in range(m):
    yy = (y[i], i + 1)
    y[i] = yy
y.sort()

i = 0
j = shi = 1
sho = []
for i in range(n):
    sh = abs(x[i][0] - y[0][0])
    for j in range(shi - 1, m):
        if abs(x[i][0] - y[j][0]) <= sh:
            sh = abs(x[i][0] - y[j][0])
            shi = y[j][1]
        else:
            break
    sho.append((x[i][1], shi, sh))
print(sho)
sho.sort()
print(sho)

for i in range(n):
    print(sho[i][1], end=' ')
