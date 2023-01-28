"""mapper.py"""
import sys
import re

wordMap = {}
rgx = re.compile(r'[A-Za-z]+')

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if rgx.match(word) is not None:
            if wordMap.get(word) is not None:
                wordMap[word] += 1
            else:
                wordMap[word] = 1

for word, count in wordMap.items():
    print ('%s\t%s' % (word, count))
