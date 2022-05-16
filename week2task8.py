A, B, C, D, E = int(input()), int(input()), int(input()), \
                int(input()), int(input())
if (D >= A and (E >= B or E >= C)) or \
        (D >= B and (E >= A or E >= C)) or (D >= C and (E >= A or E >= B)):
    print('YES')
else:
    print('NO')
