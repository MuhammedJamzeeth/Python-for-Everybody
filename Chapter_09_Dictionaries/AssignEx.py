name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
nFile = open(name)
counts = dict()

for line in nFile:
    line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        # if key is not there the count is zero
        oldCount = counts.get(word, 0)
        print(word, 'old', oldCount)
        newCount = oldCount + 1
        counts[word] = newCount
        print(word, 'new', newCount)

print(counts)
