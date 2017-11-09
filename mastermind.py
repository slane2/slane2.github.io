import random
options = ('R','G','B','P')
first = random.choice(options)
second = random.choice(options)
third = random.choice(options)
fourth = random.choice(options)
computer=[first, second, third, fourth]
print(computer)
human= input('Make a guess')
human=list(human)
count=0
for i in range(4):
    if computer == human:
        print('Huzzah!')
        break
for i in range(4):
    if computer[i]==human[i]:
        Q=human[i]
        X=computer[i]
        count=count+1
print("B"*count)
print(computer)
print(human)
for i in range (4):
    if human[0]==computer[i]:
        S=human[0]
        print("W")
for i in range (4):
    if human[1]==computer[i]:
        print("W")
        T=human[1]
for i in range (4):
    if human[2]==computer[i]:
        print("W")
        U=human[2]
for i in range (4):
    if human[3]==computer[i]:
        print("W")
        V=human[3]
