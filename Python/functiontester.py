count=0
x="ssss"
y="ssssss"

for i in range (len(y)-len(x)+1):
    print(i)
    print(y[i:i+len(x)])
    if x == y[i:i+len(x)]:
        count=count+1
print("count = " + str(count))
