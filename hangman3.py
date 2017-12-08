from random import randint
#import random
def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        #count = 0
        #for line in wordFile:
         #   if len(line) > 4 and len(line) < 7:
          #      wordList.append(line[0:-1])
        #for(i=randrange(0,980); i < len(wordFile); i++)
        #num=randint(0,980)
        #for item in wordFile:
        #   print(type(item))
        #   if len(item) > 4 and len(item) < 7:
        #        wordList.append(item[0:-1])
        #        return wordList
        arrayOfWords = []
        for item in wordFile:
            arrayOfWords.append(item)

        hangmanWord = arrayOfWords[randint(0,100)]
        return hangmanWord
#word = str([2:len(str(readWords()))-1])
#word = readWords()
#print(type(word))
#word = word[2:len(word)-2]
#word="hello"
#print(word)
#print(len(word))
word = readWords()
print(word)

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
    
