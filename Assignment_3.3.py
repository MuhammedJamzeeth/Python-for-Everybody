score = input("Enter Score: ")
s = float(score)

if 0.0 < s < 1.0:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Out of Range (enter btw 0.0 and 1.0')
