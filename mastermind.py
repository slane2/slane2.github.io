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
for i in range(4):
    if computer == human:
        print('Huzzah!')
        break
for i in range(1):
    if computer==human:
        Q=human[0]
        print("B")
for i in range(1,2):
    if computer==human:
        X=human[1]
        print("B")
for i in range(2,3):
    if computer[2]==human[2]:
        Y=human[2]
        print("B")
for i in range(3,4):
    if computer[3]==human[3]:
        Z=human[3]
        print("B")
