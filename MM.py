import random
options = ('R','G','B','P')
human= input('Make a guess')
first = random.choice(options)
second = random.choice(options)
third = random.choice(options)
fourth = random.choice(options)
computer=[first, second, third, fourth]
for i in range(4):
    if computer == human:
        print('Huzzah!')
        break
    elif computer[0]==human[0]:
        Q=human[0]
        print("B")
    elif computer[1]==human[1]:
        X=human[1]
        print("B")
    elif computer[2]==human[2]:
        Y=human[2]
        print("B")
    elif computer[3]==human[3]:
        Z=human[3]
        print("B")
