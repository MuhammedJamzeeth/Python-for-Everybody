fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    sLines = line.split()
    for sLine in sLines:
        if sLine in lst:
            continue
        lst.append(sLine)
lst.sort()
print(lst)
