class Pupil:
    surname = ' '
    name = ' '
    number = ' '
    r = ' '


inFile = open('input.txt', 'r', encoding='utf8')
pupils = inFile.readlines()
inFile.close()
i = 0
for line in pupils:
    student = list(map(str, line.split()))
    Pupil.surname = student[0]
    Pupil.name = student[1]
    Pupil.number = student[2]
    Pupil.r = student[3]
    pupils[i] = Pupil
    i = i + 1

for i in range(len(pupils)):
    pupils.sort(key=lambda pupils: pupils[i].surname)
print(pupils)

outFile = open('output.txt', 'w', encoding='utf8')

outFile.close()
