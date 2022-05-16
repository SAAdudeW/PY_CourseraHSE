# filter(condition, iterable)
# enumerate(iterable)
# zip(iterable 1, iterable 2,..)
# no for allowed
from sys import stdin


def splitf(string):
    return string.split()


print(list(map(splitf, stdin.readlines())))  # список из списков из слов строк
