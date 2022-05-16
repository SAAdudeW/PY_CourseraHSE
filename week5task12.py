string = input()
numList = list(map(int, string.split()))
for i in range(1, len(numList), 2):
    numList.insert(i - 1, numList[i])
    numList.pop(i + 1)
for i in range(0, len(numList)):
    print(numList[i], end=' ')
