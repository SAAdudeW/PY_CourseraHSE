from sys import stdin

cDict = {}
n = 0
b = 0
c = 0
for line in stdin:
    liner = line.split('\n')
    if c == 0:
        n = int(liner[0])
    elif liner[0].isalpha():
        cDict[liner[0]] = cDict.get(liner[0], 0) + 1
        if cDict[liner[0]] == n:
            b += 1
    c += 1

print(b)
for language in cDict:
    if cDict[language] == n:
        print(language)

print(len(cDict))
for language in cDict:
    print(language)
