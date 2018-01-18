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
        elif computer[i]==human[i]:
            human[i]="T"
            computer[i]="L"
            count=count+1

        elif human[i]==computer[i]:
            human[i]="S"
            count=count+1
    
    Y=("partial "*count)
    X=(4-count)
    X=("full "*X)
    Z=(X+Y)
    print(Z)
    computer=list(originalcomputer)
    
    if human==originalcomputer:
        break
