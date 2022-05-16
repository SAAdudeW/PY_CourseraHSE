from sys import stdin

c, N = 0, 0
syns = {}
for line in stdin:

    if c == 0:
        N = int(line)

    if 1 <= c <= N:
        words = line.split()
        syns[words[1]] = words[0]
        syns[words[0]] = words[1]

    if c == N + 1:
        word = line.split()
        print(syns.get(word[0], 0))

    c += 1
