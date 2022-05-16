from sys import stdin

any(filter(lambda y: y == 0, list(map(int, map(lambda x: x.split(), stdin.readlines())))))
