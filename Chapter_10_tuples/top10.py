fHand = open('romeo.txt')
counts = dict()

for line in fHand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newTup = (val, key)
    lst.append(newTup)

lst = sorted(lst, reverse=False)

for val, key in lst[:10]:
    print(key, val)

print(sorted([(v, k) for k, v in counts.items()]))
