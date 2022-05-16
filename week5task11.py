m = d = 2000
n = int(input())
string = input()
numList = list(map(int, string.split()))
x = int(input())
for i in range(0, n):
    if abs(numList[i] - x) <= d:
        d = abs(numList[i] - x)
        m = numList[i]
print(m)
