fr = open('input.txt', 'r', encoding='utf8')
pupilListSq = []
for line in fr:
    pupilString = line
    pupilList = list(pupilString.split())
    pupilListSq.append(pupilList)
fr.close()
pupilListSq.sort(key=lambda l: l[0])

fw = open('output.txt', 'w', encoding='utf8')
for pupilList in pupilListSq:
    pupil = pupilList[0] + ' ' + pupilList[1] + ' ' + pupilList[3]
    print(pupil, file=fw)
fw.close()
