import random


class Node:
    def __init__(self):
        self.count = 0
        self.children = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    def incCount(self):
        self.count += 1


class Trie:
    def __init__(self) -> None:
        self.root = Node()
        self.wordCount = 0
    def add(self, word):
        traverseNode = self.root
        for i in range(0, len(word)):
            index = ord(word[i]) - ord('a')
            if traverseNode.children[index] is None:
                traverseNode.children[index] = Node()
            traverseNode = traverseNode.children[index]

        if traverseNode.count == 0:
            traverseNode.incCount()
            self.wordCount += 1
    
    def getWordCount(self):
        return self.wordCount
    def check(self, word):
        traverseNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            if traverseNode.children[index] is not None:
                traverseNode = traverseNode.children[index]
            else:
                return False
        if traverseNode.count != 0:
            return True
        else:
            return False
    def checkSubstring(self, word):
        traverseNode = self.root
        for char in word:
            index = ord(char) - ord('a')
            if traverseNode.children[index] is not None:
                traverseNode = traverseNode.children[index]
            else:
                return False
        return True

            



class charNode:
    def __init__(self, usedLetters, letterPosition, substring):
        self.usedLetters = usedLetters
        self.children = []
        self.letterPosition = letterPosition
        self.substring = substring
    def addChild(self, charNode):
        self.children.append(charNode)


def stringTranslate(string):
    word = ''
    for char in string:
        word = word + board[char[0]][char[1]]
    return word

def checkLetter(letter, tempCharNode):
    tempString = tempCharNode.substring.copy()
    tempString.append(letter)
    word = stringTranslate(tempString)
    if dictionary.checkSubstring(word):
        usedLetters = tempCharNode.usedLetters.copy()
        usedLetters.add(letter)
        newCharNode = charNode(usedLetters, letter, tempString)
        tempCharNode.addChild(newCharNode)
        if dictionary.check(word):
            if word not in foundWords:
                print(word)
            foundWords.add(word)
            

def wordRecurse(tempCharNode):
    i = tempCharNode.letterPosition[0]
    j = tempCharNode.letterPosition[1]
    if i+1 < 5 and j-1 > -1 and (i+1, j-1) not in tempCharNode.usedLetters:
        letter = (i+1, j-1)
        checkLetter(letter, tempCharNode)
    if i+1 < 5 and (i+1, j) not in tempCharNode.usedLetters:
        letter = (i+1, j)
        checkLetter(letter, tempCharNode)
    if i+1 < 5 and j+1 < 5 and (i+1, j+1) not in tempCharNode.usedLetters:
        letter = (i+1, j+1)
        checkLetter(letter, tempCharNode)
    if j-1 > -1 and (i, j-1) not in tempCharNode.usedLetters:
        letter = (i, j-1)
        checkLetter(letter, tempCharNode)
    if j+1 < 5 and (i, j+1) not in tempCharNode.usedLetters:
        letter = (i, j+1)
        checkLetter(letter, tempCharNode)
    if i-1 > -1 and j-1 > -1 and (i-1, j-1) not in tempCharNode.usedLetters:
        letter = (i-1, j-1)
        checkLetter(letter, tempCharNode)
    if i-1 > -1 and (i-1, j) not in tempCharNode.usedLetters:
        letter = (i-1, j)
        checkLetter(letter, tempCharNode)
    if i-1 > -1 and j+1 < 5 and (i-1, j+1) not in tempCharNode.usedLetters:
        letter = (i-1, j+1)
        checkLetter(letter, tempCharNode)
    for childNode in tempCharNode.children:
        wordRecurse(childNode)


dice = {
    ('p', 't', 'e', 'l', 'c', 'i'),
    ('n', 'n', 'n', 'e', 'a', 'd'),
    ('e', 'e', 'u', 'g', 'm', 'a'),
    ('h', 'r', 'l', 'h', 'o', 'd'),
    ('o', 'o', 't', 'o', 'u', 't'),
    ('p', 'i', 'e', 'c', 't', 's'),
    ('r', 'i', 's', 'f', 'a', 'a'),
    ('t', 'o', 't', 't', 'e', 'm'),
    ('j', 'k', 'b', 'x', 'z', 'qu'),
    ('e', 't', 'i', 't', 'i', 'i'),
    ('a', 'e', 'm', 'e', 'e', 'e'),
    ('r', 'l', 'h', 'n', 'o', 'd'),
    ('f', 's', 'y', 'r', 'i', 'p'),
    ('a', 'e', 'a', 'e', 'e', 'e'),
    ('t', 'n', 'u', 'w', 'o', 'o'),
    ('n', 'h', 'd', 't', 'd', 'o'),
    ('o', 'n', 'd', 'l', 'r', 'h'),
    ('r', 'y', 's', 'f', 'a', 'i'),
    ('i', 'e', 'c', 'i', 't', 'l'),
    ('r', 'g', 'v', 'r', 'w', 'o'),
    ('r', 'i', 'r', 'p', 'r', 'y'),
    ('f', 's', 'a', 'r', 'a', 'a'),
    ('m', 'e', 'n', 'n', 'g', 'a'),
    ('u', 's', 'e', 's', 's', 'n'),
    ('c', 'e', 'n', 'c', 's', 'h')
}

dictionary = Trie()
# Need a dictionary file to draw from
smallFilePath = 'C:/Users/18102/Puzzles/smallDictionary.txt'
medFilePath = 'C:/Users/18102/Puzzles/mediumDictionary.txt'
largeFilePath = 'C:/Users/18102/Puzzles/english3.txt'
dictionaryFile = open(medFilePath, 'r')
words = dictionaryFile.readlines()
print('Filling Dictionary')
for word in words:
    word = word.strip()
    if len(word) >= 3 and word.isalpha():
        dictionary.add(word)
print('Dictionary has', dictionary.getWordCount(), 'words')


userAddingBoard = input('input board y/n?  ')

if userAddingBoard == 'y':
    # User Inputs the board one letter at a time from left to right, top to bottom
    board = []
    for i in range(0, 5):
        board.append([])
        for j in range(0, 5):
            board[i].append(input('Enter Next Letter: '))


else:
    # Randomly generate a board
    board = [[], [], [], [], []]
    for row in board:
        for i in range(0, 5):
            tempDice = []
            for die in dice:
                tempDice.append(die)
            die = random.choice(tempDice)
            row.append(random.choice(die))
            dice.remove(die)


# This is the board we played
# board = [['p', 'n', 'e', 'h', 'o'],
#          ['p', 'r', 't', 'j', 'e'],
#          ['a', 'r', 'f', 'a', 't'],
#          ['n', 'o', 'r', 'i', 'r'],
#          ['r', 'f', 'm', 'u', 'c']]

foundWords = set()
# Loop over each letter in the board and start the recursive search process
for x in range(0, len(board)):
    for y in range(0, len(board[x])):
        usedLetters = set()
        usedLetters.add((x, y))
        rootCharNode = charNode(usedLetters, (x,y), [(x,y)])
        wordRecurse(rootCharNode)

for row in board:
    print(row)

print(len(foundWords))





































# The following code runs n number of games and prints out the word count distribution of those games.

# counts = []
# maxCount = 0
# minCount = 1000
# for n in range(0, 1000000):
#     if n % 500 == 0:
#         print(n)
#     dice = {
#         ('p', 't', 'e', 'l', 'c', 'i'),
#         ('n', 'n', 'n', 'e', 'a', 'd'),
#         ('e', 'e', 'u', 'g', 'm', 'a'),
#         ('h', 'r', 'l', 'h', 'o', 'd'),
#         ('o', 'o', 't', 'o', 'u', 't'),
#         ('p', 'i', 'e', 'c', 't', 's'),
#         ('r', 'i', 's', 'f', 'a', 'a'),
#         ('t', 'o', 't', 't', 'e', 'm'),
#         ('j', 'k', 'b', 'x', 'z', 'qu'),
#         ('e', 't', 'i', 't', 'i', 'i'),
#         ('a', 'e', 'm', 'e', 'e', 'e'),
#         ('r', 'l', 'h', 'n', 'o', 'd'),
#         ('f', 's', 'y', 'r', 'i', 'p'),
#         ('a', 'e', 'a', 'e', 'e', 'e'),
#         ('t', 'n', 'u', 'w', 'o', 'o'),
#         ('n', 'h', 'd', 't', 'd', 'o'),
#         ('o', 'n', 'd', 'l', 'r', 'h'),
#         ('r', 'y', 's', 'f', 'a', 'i'),
#         ('i', 'e', 'c', 'i', 't', 'l'),
#         ('r', 'g', 'v', 'r', 'w', 'o'),
#         ('r', 'i', 'r', 'p', 'r', 'y'),
#         ('f', 's', 'a', 'r', 'a', 'a'),
#         ('m', 'e', 'n', 'n', 'g', 'a'),
#         ('u', 's', 'e', 's', 's', 'n'),
#         ('c', 'e', 'n', 'c', 's', 'h')
#     }
#     board = [[], [], [], [], []]
#     for row in board:
#         for i in range(0, 5):
#             tempDice = []
#             for die in dice:
#                 tempDice.append(die)
#             die = random.choice(tempDice)
#             row.append(random.choice(die))
#             dice.remove(die)
    
#     foundWords = set()
#     for x in range(0, len(board)):
#         for y in range(0, len(board[x])):
#             usedLetters = set()
#             usedLetters.add((x, y))
#             rootCharNode = charNode(usedLetters, (x,y), [(x,y)])
#             wordRecurse(rootCharNode)

#     # for row in board:
#     #     print(row)
#     count = len(foundWords)
#     # print(count)
#     counts.append(count)
#     if count > maxCount:
#         maxCount = count
#     if count < minCount:
#         minCount = count

# sum = 0
# for count in counts:
#     sum += count
# average = sum / len(counts)
# print('average:', average)
# print('min:', minCount)
# print('max:', maxCount)

# step = 25
# for i in range(-10, 500, step):
#     stepCount = 0
#     for count in counts:
#         if count > i and count <= i + step:
#             stepCount += 1
#     print(i, '-', i+step, ': ', stepCount)