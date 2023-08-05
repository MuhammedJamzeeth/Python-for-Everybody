a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)

# Building a list from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Is something in a List
some = [1, 9, 21, 10, 16]
var = 9 in some
print(var)
var = 20 not in some
print(var)
print(15 in some)

# List are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])
