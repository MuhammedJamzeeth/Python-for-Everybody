# The get method for dictionaries
counts = dict()
names = ['cssv', 'cwen', 'csev', 'zqian', 'cwen']

# if name in counts:
#     x = counts[name]
# else:
#     x = 0

# x = counts.get(name, 0)
# print(x)

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
