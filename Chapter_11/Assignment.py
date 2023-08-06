import re

nList = list()

handle = open('words.txt')
for line in handle:
    line = line.rstrip()
    n = re.findall('[0-9]+', line)
    if len(n) > 0:
        # print(n)
        for x in n:
            xf = int(x)
            nList.append(xf)

# print(nList)
tot = sum(nList)
print(tot)
