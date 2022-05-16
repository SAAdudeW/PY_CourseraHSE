string = input()
numList = list(map(int, string.split()))
m = mm = numList[0]
im = imm = 0
for i in range(1, len(numList)):
    if m < numList[i]:
        m = numList[i]
        im = i
    if mm > numList[i]:
        mm = numList[i]
        imm = i
numList.insert(im, mm)
numList.pop(im + 1)
numList.insert(imm, m)
numList.pop(imm + 1)
for i in range(0, len(numList)):
    print(numList[i], end=' ')
