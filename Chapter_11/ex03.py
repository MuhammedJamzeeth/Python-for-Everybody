# Matching and Extracting Data
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    y = re.findall('[AEIOU]+', line)
    e = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
    if len(y) > 0:
        print(y)
    if len(e) > 0:
        print(e)
