def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)


a, b = int(input()), int(input())
print(sum(a, b))


def SeqSum():
    n = int(input())
    if n != 0:
        return n + SeqSum()
    else:
        return 0


print(SeqSum())


def sequence():
    a = int(input())
    if a != 0:
        sequence()
    print(a)


sequence()
