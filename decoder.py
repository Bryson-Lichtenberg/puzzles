from string import ascii_lowercase
import sys


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

namesFile = open("C:/Users/18102/Puzzles/lastNames.txt", 'r')
names = namesFile.readlines()
print(len(names), 'Names')


count = 0
for name in names:
    count += 1
    # if count % 1000 == 0:
    #     print(count)
    cipher = []
    alphabetSet = set()
    for char in name:
        if char not in alphabetSet and char.isalnum():
            cipher.append(char.lower())
            alphabetSet.add(char.lower())
    for c in ascii_lowercase:
        if c not in alphabetSet:
            cipher.append(c)
            alphabetSet.add(c)
    # print(cipher)
    # print(len(cipher))

    code = [[4, 12, 24], [4, 2, 23, 2, 16], [17, 16, 2], [2, 12, 10, 11, 21]]
    outPhrase = []
    for word in code:
        outWord = ''
        for char in word:
            outWord = outWord + cipher[char - 1]
        outPhrase.append(outWord)


    foundWords = True
    for word in outPhrase:
        if not dictionary.checkSubstring(word):
            foundWords = False
    if foundWords:
        print(count)
        print(name)
        for word in outPhrase:
            print(word)
    # print(name)
    # for word in outPhrase:
    #     print(word)
    # sys.exit()





# This is the code to be deciphered
# (4 12 24) (4 2 23 2 16) (17 16 2) (2 12 10 11 21)