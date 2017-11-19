from random import randint
options=('Rock','Paper', 'Scissors')
human= input('Rock, Paper, or Scissors?')
computer=options[randint(0,2)]
print(computer)
if human==computer:
    print('Tie!');
elif human=='Rock' and computer=='Paper':
    print("Sorry Sucka!");
elif human=='Rock' and computer=='Scissors':
    print('You Win!');
elif human=='Paper' and computer=='Scissors':
    print('Sorry Sucka!');
elif human=='Paper' and computer=='Rock':
    print('You Win!');
elif human=='Scissors' and computer=='Rock':
    print('Sorry Sucka!');
elif human=='Scissors' and computer=='Paper':
    print('You Win!');
