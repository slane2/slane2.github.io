"""
   Hangman
     Plays a basic game of hangman
    
   Author:  JJ Programmer
   Version: 0.01
   Date:    11/07/2017
"""

import random

def makeArt():
    art = []
    art.append('         +---------+') #line 0
    art.append('         |         |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append(' ------------------+')
    return art

def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 4 and len(line) < 7:
                wordList.append(line[0:-1])
            
    return wordList

def printArt(art):
    for line in art:
        print(line)

def setParts(): #dictionary of functions
    parts = {
        1 : head,
        2 : body,
        3 : leftArm,
        4 : rightArm,
        5 : leftLeg,
        6 : rightLeg,
        }
    return parts

def head(art):
    art.insert(2, '       +---+       |');
    art.insert(2, '       +   +       |');
    art.insert(2, '       +---+       |');

def body(art):
    art.insert(5, '      +-----+      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +-----+      |');
    art.insert(5, '         +         |');

def leftArm(art):
    pass

def rightArm(art):
    pass

def leftLeg(art):
    pass

def rightLeg(art):
    pass

def init():
    bodyParts = setParts()
    art = makeArt()
    words = readWords()
    return bodyParts, art, words

def main():
    bodyParts, art, words = init()
    
    printArt(art)
    
    misses = 1
    bodyParts[misses](art)   #call to function art
    
    misses = 2
    bodyParts[misses](art)
    
    printArt(art);
    
    for i in range(20):
        print(random.choice(words))

#main()


def f(x): #assumes x is list
    for line in x:
        print(line)
def insertLetter(spaces, letter, pos):
    #_ _ _ _ ....
    #0123456 ....
    # pos * 2 --> location in spaces
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos + 1:]
    return spaces
word = random.choice(readWords())

pic = [0,0,0,0,0]
pic[0] = '==========='
pic[1] = '=         ='
pic[2] = '=    +    ='
pic[3] = '==========='


spaces = "_ " * len(word)

def printPic(x): #assumes x is list
    for line in x:
        print(line)

for i in range(len(word)):
    guess = input("letter? ")

    if guess in word:
        pos = word.index(guess)
        spaces = insertLetter(spaces, guess, pos)
    else:
        print("nope")

    pic[4] = spaces
    printPic(pic)
    
