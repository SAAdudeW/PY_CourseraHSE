k = int(input())
inData = open('input.txt', 'r', encoding='utf8')
applicants = inData.readlines()
inData.close()


class Pupil:
    name = ' '
    surname = ' '
    first = 0
    second = 0
    third = 0


def summa(person):
    return person.first + person.second + person.third


sorting = [0] * 181
for person in applicants:
    tempMan = person.split()
    man = Pupil()
    man.first = int(tempMan[2])
    man.second = int(tempMan[3])
    man.third = int(tempMan[4])
    if man.first < 40 or man.second < 40 or man.third < 40:
        continue
    person = man
    sorting[summa(person) - 120] += 1

s = 0
for i in range(180, -1, -1):
    if s < k:
        s += sorting[i]
        si = i
    else:
        break

outData = open('output.txt', 'w', encoding='utf8')
if k >= len(applicants):
    print(0)
    print(0, file=outData)
elif sorting[180] > k:
    print(1)
    print(1, file=outData)
else:
    print(120 + si)
    print(120 + si, file=outData)
outData.close()
