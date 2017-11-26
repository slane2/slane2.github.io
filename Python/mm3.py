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
for i in range(1):
    if human[0]==computer[1]:
        S=human[0]
    print("W")
for i in range (1):
    if human[0]==computer[2]:
        print("W")
        T=human[0]
for i in range (1):
    if human[0]==computer[3]:
        print("W")
        U=human[0]
for i in range(1,2):
    if human[1]==computer[0]:
        print("W")
        U=human[0]
for i in range (1,2):
    if human[1]==computer[2]:
        print("W")
        V=human
for i in range (1,2):
    if human [1]==computer[3]:
        print("W")
        L=human[1]
for i in range (2,3):
    if human[2]==computer[0]:
        print("W")
        N=human[2]
for i in range(2,3):
    if human[2]==computer[1]:
        print("W")
    O=human[2]
for i in range (2,3):
    if human[2]==computer[3]:
        print("W")
        A=human[2]
for i in range (3,4):
    if human[3]==computer[0]:
        print("W")
        C=human[3]
for i in range (3,4):
    if human[3]==computer[1]:
        print("W")
        D=human[3]
for i in range (3,4):
    if human[3]==computer[2]:
        print("W")
        E=human[3]
