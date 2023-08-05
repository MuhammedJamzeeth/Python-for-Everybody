n = 5
while n > 0:
    print(n)
    n = n - 1

print('Blastoff')
print(n)

# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('Blastoff')

friends = ['Joesph', 'Glen', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

print('Done!')

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

print('After', smallest)
