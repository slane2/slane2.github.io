import random
def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 7 and len(line) < 10:
                wordList.append(line[0:-1])
                return wordList
word = readWords()
secretWord=random.choice(word)
print(secretWord)

def insertLetter(spaces, letter, pos):
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos + 1:]
    return spaces



spaces = "_ " * len(word)


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



def printPic(x):
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

    
