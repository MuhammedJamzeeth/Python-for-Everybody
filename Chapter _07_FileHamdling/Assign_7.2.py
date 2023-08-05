# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
Tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    line.rstrip()
    txt = line.find(':')
    noTxt = line[txt + 1:]
    noFlo = float(noTxt)
    Tot = Tot + noFlo
    count = count + 1

avg = Tot / count
print('Average spam confidence:', avg)
