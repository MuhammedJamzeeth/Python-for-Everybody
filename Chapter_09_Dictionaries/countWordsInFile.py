name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = 0
bigWord = 0
for word, count in counts.items():
    if count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)
