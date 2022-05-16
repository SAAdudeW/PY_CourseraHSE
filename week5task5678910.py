string = input()
numList = list(map(int, string.split()))
print(' '.join(map(str, numList[0::2])))

string = input()
numList = list(map(int, string.split()))
for i in range(0, len(numList)):
    if numList[i] % 2 == 0:
        print(numList[i], end=' ')

string = input()
numList = list(map(int, string.split()))
c = 0
for i in range(0, len(numList)):
    if numList[i] > 0:
        c = c + 1
print(c)

string = input()
numList = list(map(int, string.split()))
im = 0
m = numList[0]
for i in range(0, len(numList)):
    if numList[i] >= m and i > im:
        m = numList[i]
        im = i
print(m, im)

string = input()
numList = list(map(int, string.split()))
for i in range(1, len(numList)):
    if numList[i] > numList[i - 1]:
        print(numList[i], end=' ')

string = input()
numList = list(map(int, string.split()))
m = 1000
for i in range(1, len(numList)):
    if 0 < numList[i] < m:
        m = numList[i]
print(m)
