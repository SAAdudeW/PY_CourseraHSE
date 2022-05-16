inp = list(map(int, input().split()))
data = [0]
for i in range(inp[1]):
    if i == 0:
        data[0] = int(input())
    else:
        data.append(int(input()))
data.sort()
k = 0
ss = 0
for i in range(inp[1]):
    ss = ss + data[i]
    if ss <= inp[0]:
        k = k + 1
    else:
        break
print(k)
