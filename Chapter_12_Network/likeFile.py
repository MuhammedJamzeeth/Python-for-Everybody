import urllib.request

fHand = urllib.request.urlopen('https://paravi.ruh.ac.lk/index.html')

counts = dict()
for line in fHand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
