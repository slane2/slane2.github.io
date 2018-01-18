import random
options = ('R','G','B','P')
first = random.choice(options)
second = random.choice(options)
third = random.choice(options)
fourth = random.choice(options)
computer=[first, second, third, fourth]
originalcomputer=list(computer)
print(computer)



human= "C"
while human != computer:
    human= input('Make a guess')
    human=list(human)
    count=0
    for i in range(4):
        if computer == human:
            print('Huzzah!')
            #print(computer)
            #print(human)
            break
    for i in range(4):
        if computer[i]==human[i]:
            human[i]="T"
            computer[i]="L"
            count=count+1
    Y=("B"*count)
    count1=count
   # print(computer)
    #print(human)

    for i in range (4):
        if human[0]==computer[i]:
            human[0]="S"
            count=count+1
    for i in range (4):
        if human[1]==computer[i]:
            human[1]="S"
            count=count+1
    for i in range (4):
        if human[2]==computer[i]:
            human[2]='S'
            count=count+1
    for i in range (4):
        if human[3]==computer[i]:
            human[3]="S"
            count=count+1
    
    X=(count-count1)
    X=("W"*X)
    Z=list(X+Y)
    print(Z)
    computer=list(originalcomputer)
    
    if human==originalcomputer:
        break

