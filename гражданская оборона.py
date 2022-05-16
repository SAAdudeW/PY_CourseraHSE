n = int(input())
nList = list(map(int, input().split()))
nTupleList = []
for ni in range(len(nList)):
    nTupleList.append((ni + 1, nList[ni]))
nTupleList.sort(key=lambda a: a[1])  # sorted cities

m = int(input())
mList = list(map(int, input().split()))
mTupleList = []
for mi in range(len(mList)):
    mTupleList.append((mi + 1, mList[mi]))
mTupleList.sort(key=lambda b: b[1])  # sorted shelters

core = [0] * n
mini = 1
for x in range(n):
    y = mini - 1
    t = 0
    mind = abs(nTupleList[x][1] - mTupleList[m - 1][1])
    while y < m and y < mini + 2:
        if abs(nTupleList[x][1] - mTupleList[y][1]) < mind:
            t = 1
            core[nTupleList[x][0] - 1] = mTupleList[y][0]
            mind = nTupleList[x][1] - mTupleList[y][1]
            mini = y
        if t == 0:
            core[nTupleList[x][0] - 1] = mTupleList[m - 1][0]
            mini = y
        y += 1

print(' '.join(map(str, core)))
