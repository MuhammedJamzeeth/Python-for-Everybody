fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

# Skipping with continue
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# Using in to Select lines
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
