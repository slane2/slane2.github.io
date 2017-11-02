print('Welcome to Master Mind.\n Your objective is to guess the exact sequence of four randomly generated colored pegs.\n A return of a black peg, denoted as "B" indicates an exact match of color and placement.\n A return of a "W" indicates a correct color in a wrong place.\n The order of the returned black and white pegs is not indicative of which pegs are matched.\n Enter Red "R", Blue "B", Green "G", or Purple "P" in any chosen order up to 4.\n Must denote with the capital first letter of your chosen color.\n Repeats are ok.')
import random
computer= [random.choice(['R','G','B','P'])
           for i in range(4)]


userGuess= input('Guess up to 4 colors')
userGuess=user.upper()
userGuess=list(userGuess)

if computer == userGuess:
    print('Huzzah!')

print(0(computer))


#for i in userGuess















##def mastermind(guess, computer):
 ##   guess=input('????')
#flag=[1,1,1,1]
 ##   exactMatch=0
 ##   partialMatch=0
 ##  for i in len(computer):
 ##       if guess[i] == computer[i]
 ##           flag[i]=0
 ##           exactMatch += 1
   ## print("you have" + str(exactMatch) + "exactly right")
    
    


