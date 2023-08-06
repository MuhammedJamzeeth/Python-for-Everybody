# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line.rstrip()
    ln = line.split()
    if len(ln) < 1:
        continue
    if ln[0] != 'From':
        continue
    time = ln[5]
    sTimes = time.split(':')
    pTime = sTimes[0]
    # for pTime in sTimes:
    #     counts[pTime] = counts.get(pTime, 0) + 1
    counts[pTime] = counts.get(pTime, 0) + 1
print(counts)

lst = list()
for k, v in counts.items():
    newTup = (k, v)
    lst.append(newTup)

lst = sorted(lst, reverse=False)

for v, k in lst:
    print(v, k)
