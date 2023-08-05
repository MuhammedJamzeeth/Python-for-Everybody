greet = 'Hello Bob'

nnn = greet.upper()
print(nnn)

www = greet.lower()
print(www)

# Search and Replace

nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

# Stripping Whitespace
greet = '   Hello Bob   '
greet.lstrip()
print(greet)
greet.rstrip()
print(greet)
greet.strip()
print(greet)

# Prefixes
line = 'Please have a nice day'
var = line.startswith('Please')
print(var)
var = line.startswith('p')
print(var)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atops = data.find('@')
print(atops)

sppos = data.find(' ', atops)
print(sppos)

host = data[atops + 1:sppos]
print(host)

pos = data.find('.')
print(data[pos:pos + 3])

text = "X-DSPAM-Confidence:    0.8475"
fno = text.find(':')
piece = text[fno + 1:]
value = float(piece)
print(value)
