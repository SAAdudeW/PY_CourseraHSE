class Pupil:
    surname = ' '
    rate = 0


N = int(input())
participants = [0] * N
for i in range(N):
    tempMan = input().split()
    man = Pupil()
    man.surname = tempMan[0]
    man.rate = int(tempMan[1])
    participants[i] = man

participants.sort(key=lambda man: -man.rate)

for man in participants:
    print(man.surname)
