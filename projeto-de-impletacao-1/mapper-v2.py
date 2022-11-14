"""mapper.py"""
import sys

wordMap = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if wordMap.get(word) is not None:
            wordMap[word] += 1
        else:
            wordMap[word] = 1

for word, count in wordMap.items():
    print ('%s\t%s' % (word, count))
