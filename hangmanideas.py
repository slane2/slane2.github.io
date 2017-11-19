import random
def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 4 and len(line) < 7:
                wordList.append(line[0:-1])
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

pic = [1,2,3,4,5,6,7,8,9]
pic[0] = '         +---------+'
pic[1] = '         |         |'
pic[2] = '        ( )        |'
pic[3] = '       --l--       |'
pic[4] = '      *  l  *      |'
pic[5] = '      *  l   *     |'
pic[6] = '        | |        |'
pic[7] = '        l l        |'
pic[8] = '                    '
word = random.choice(wordList)
spaces = "_ " * len(word)

def printPic(x): #assumes x is list
    for line in x:
        print(line)

#main loop
for i in range(len(word)):
    guess = input("letter? ")

    if guess in word:
        pos = word.index(guess)
        spaces = insertLetter(spaces, guess, pos)
    else:
        print("nope")

    pic[8] = spaces
    printPic(pic)
    
"""
spaces = "_ " * len(word)
print(spaces)
spaces = insertLetter(spaces, 'o', 1)
print(spaces)
spaces = insertLetter(spaces, 't', 4)
print(spaces)

guess = input("letter? ")

if guess in word:
    print("ok")
else:
    print("nope")
"""






"""
foo = [5,6,7,8,9,0]


def f(x): #assumes x is list
    for line in x:
        print(line)

f(pic)

pic[1] = '= *** *** ='
pic[2] = '= *** *** ='

f(pic)
f(foo)
"""
