fr = open('input.txt', 'r', encoding='utf8')
K = int(fr.readline())
pupils = []
for line in fr:
    pupilList = list(line.split())
    pupilScore = []
    for el in pupilList:
        if el.isdigit():
            pupilScore.append(el)
    if int(pupilScore[0]) < 40 or \
            int(pupilScore[1]) < 40 or \
            int(pupilScore[2]) < 40:
        continue
    pupilSum = int(pupilScore[0]) + int(pupilScore[1]) + int(pupilScore[2])
    pupils.append(pupilSum)
fr.close()
pupils.sort(reverse=True)

fw = open('output.txt', 'w', encoding='utf8')
if len(pupils) <= K:
    print(0, file=fw)
elif pupils.count(pupils[0]) > K:
    print(1, file=fw)
else:
    if pupils[K - 1] == pupils[K]:
        print(pupils[pupils.index(pupils[K]) - 1], file=fw)
    else:
        print(pupils[K - 1], file=fw)
fw.close()
