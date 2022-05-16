from sys import stdin

data = {}
c = 0
for line in stdin:
    candidate = line.split('\n')
    data[candidate[0]] = data.get(candidate[0], 0) + 1
    c += 1

dataReversed = {}
for key in data:
    if data[key] not in dataReversed:
        dataReversed[data[key]] = []
    dataReversed[data[key]].append(key)

s = 0
k = 0
for candidate in sorted(dataReversed, reverse=True):
    if candidate > c / 2:
        print(dataReversed[candidate][0])
        s = 1
        break
    else:
        if k == 0:
            print(dataReversed[candidate][0])
        if k == 1:
            print(dataReversed[candidate][0])
    k += 1
