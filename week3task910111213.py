s = input()
print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])
print(s[0::2])
print(s[1::2])
print(s[-1::-1])
print(s[-1::-2])
print(len(s))

s = input()
if s.find('f') != -1:
    print(s.find('f'))
if s.rfind('f') != s.find('f'):
    print(s.rfind('f'))

s = input()
m = s.find('h')
n = s.rfind('h')
s = s[:m] + s[n + 1:]
print(s)

s = input()
if s.find('f') == -1:
    print(-2)
if s.find('f') != -1:
    pos = s.find('f') + 1
    if s.find('f', pos) == -1:
        print(-1)
    else:
        print(s.find('f', pos))

s = input()
i = s.find(' ')
s = s[i + 1:] + ' ' + s[0:i]
print(s)
