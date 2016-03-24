#!/usr/bin/python
from collections import Counter
with open('access.log') as infile:
    count = Counter(line.split('-', 1)[0].strip() for line in infile)
print count.most_common(10)
