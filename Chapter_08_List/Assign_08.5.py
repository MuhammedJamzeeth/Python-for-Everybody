fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    sLine = line.split()
    if len(sLine) < 1:
        continue
    if sLine[0] != 'From':
        continue
    nLine = sLine[1]
    count = count + 1
    print(nLine)

print("There were", count, "lines in the file with From as the first word")
