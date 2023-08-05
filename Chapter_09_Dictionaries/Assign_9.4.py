# 9.4 Write a program to read through the mbox-short.
# txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committe

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
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue
    person = words[1]
    for word in words:
        if word is person:
            counts[person] = counts.get(person, 0) + 1

print(counts)

Max = 0
MaxKey = None
for k, v in counts.items():
    if v > Max:
        Max = v
        MaxKey = k

print(MaxKey, Max)
