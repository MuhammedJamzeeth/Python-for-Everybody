abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

line = 'first:second:third'
thing = line.split()
print(thing)
thing = line.split(':')
print(thing)
