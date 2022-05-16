from sys import stdin

A = B = set()
c = 1
for line in stdin:
    if c == 1:
        n = int(line)
        A = set(range(1, n + 1))
    elif line == 'HELP\n':
        break
    elif c % 2 == 0:
        B = set(map(int, line.split()))
    else:
        if line == 'YES\n':
            A &= B
        else:
            A -= B
    c += 1

print(' '.join(map(str, sorted(A))))
