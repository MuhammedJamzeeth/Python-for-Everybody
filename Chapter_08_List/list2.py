# total = 0
# count = 0
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total / count
# print(average)

numList = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print('Average:', average)
