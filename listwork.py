x=[] #empty list
x.append('A')
print(x)
y=['B','C','D']
x=x+y
print(x)
y.append('T')
print(x,y)
z=y
z.append('S')
print(y,z)
for unit in y:
	print(unit)
