import array

def read_data(filename):
	f = open(filename)
	a = []
	b = []
	line = f.readline()
	while line:
		c = line.split(' ')
		a.append(c[0])
		b.append(c[1])
		line = f.readline()
	return a,b

def find_word(a,B):
	if a in B:
		return 1
	else:
		return 0

[x1,y1] = read_data('vocab.txt')
[x2,y2] = read_data('data.out2.txt')
y1 = float(y1)
y2 = float(y2)

for a in x1:
	if find_word(a,x2) ==1:
		y2[x2.index(a)] = y2[x2.index(a)] + y1[x1.index(a)]
	else:
		x2.append(a)
		y2.append(y1[x1.index(a)])

print x2,y2
r = []
for i in range(len(x2)):
	r.append(x2[i] + ' ' + y2[i])
with open('vocab','w') as fid:
	fid.writelines(r)