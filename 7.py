from sys import stdin

wordsDict = {}
for line in stdin:
    words = line.split()
    for word in words:
        print(wordsDict.get(word, 0), end=' ')
        wordsDict[word] = wordsDict.get(word, 0) + 1
