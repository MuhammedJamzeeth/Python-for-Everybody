# Sorting Lists of Tuples

d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
print(sorted(d.items()))

# Sort by Values Instead of Key

temp = list()
for k, v in d.items():
    temp.append((v, k))

print(temp)

temp = sorted(temp, reverse=True)
print(temp)
