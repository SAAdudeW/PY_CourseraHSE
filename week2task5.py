n = int(input())
if 10 < n < 20 or n % 10 == 0 or n % 10 == 5 \
        or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9:
    print(n, 'korov')
elif n % 10 == 1 and (n < 10 or n > 20):
    print(n, 'korova')
else:
    print(n, 'korovy')
