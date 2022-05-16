from sys import stdin

wordsDict = {}
max = 0
for line in stdin:
    words = line.split()
    for word in words:
        wordsDict[word] = wordsDict.get(word, 0) + 1
        if max < wordsDict[word]:
            max = wordsDict[word]

wordsDictReversed = {}
for key in wordsDict:
    if wordsDict[key] not in wordsDictReversed:
        wordsDictReversed[wordsDict[key]] = []
    wordsDictReversed[wordsDict[key]].append(key)

for key in wordsDictReversed:
    if key == max:
        print(sorted(wordsDictReversed[key])[0])
        break
