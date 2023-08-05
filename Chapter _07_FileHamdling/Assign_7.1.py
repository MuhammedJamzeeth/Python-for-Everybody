# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fl = fh.read()
fl.rstrip()
print(fl.upper())
