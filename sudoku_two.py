from math import floor
from traceback import print_tb
import copy

board = [[[8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [6], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [5], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [8]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

board_a = copy.deepcopy(board)
board_b = copy.deepcopy(board)

solved= [[9, 2, 8, 4, 1, 3, 7, 5, 6],
         [4, 7, 5, 6, 8, 2, 3, 1, 9],
         [3, 1, 6, 7, 9, 5, 4, 8, 2],
         [8, 6, 2, 3, 5, 4, 1, 9, 7],
         [5, 3, 1, 2, 7, 9, 8, 6, 4],
         [7, 4, 9, 1, 6, 8, 5, 2, 3],
         [6, 8, 4, 9, 3, 1, 2, 7, 5],
         [1, 9, 3, 5, 2, 7, 6, 4, 8],
         [2, 5, 7, 8, 4, 6, 9, 3, 1]]

rowNeeds = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]

colNeeds = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]

sectorNeeds =  [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]]

def printNeeds():
    print("Row Needs")
    for row in rowNeeds:
        print(row)
    print("Col Needs")
    for col in colNeeds:
        print(col)
    print("Sector Needs")
    for sector in sectorNeeds:
        print(sector)

def checkMistakes():
    mistakes = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if len(board[x][y]) == 1:
                if board[x][y][0] != solved[x][y]:
                    mistakes += 1
    return mistakes


def reduceSpot(x, y):
    for a in range(0, 9):
        for b in range(0, 9):
            if(a == x and b != y):
                if len(board[a][b]) == 1:
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            if(b == y and a != x):
                if len(board[a][b]) == 1:
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            if((floor(y/3) + 3*floor(x/3)) == (floor(b/3) + 3*floor(a/3)) and (a != x and b != y)):
                if(len(board[a][b]) == 1):
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            

def reduceBoard():
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board[x][y]) > 1):
                reduceSpot(x, y)


def reduceSpot_a(x, y):
    for a in range(0, 9):
        for b in range(0, 9):
            if(a == x and b != y):
                if len(board_a[a][b]) == 1:
                    if(board_a[x][y].__contains__(board_a[a][b][0])):
                        board_a[x][y].remove(board_a[a][b][0])
            if(b == y and a != x):
                if len(board_a[a][b]) == 1:
                    if(board_a[x][y].__contains__(board_a[a][b][0])):
                        board_a[x][y].remove(board_a[a][b][0])
            if((floor(y/3) + 3*floor(x/3)) == (floor(b/3) + 3*floor(a/3)) and (a != x and b != y)):
                if(len(board_a[a][b]) == 1):
                    if(board_a[x][y].__contains__(board_a[a][b][0])):
                        board_a[x][y].remove(board_a[a][b][0])
            

def reduceBoard_a():
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board_a[x][y]) > 1):
                reduceSpot_a(x, y)


def reduceSpot_b(x, y):
    for a in range(0, 9):
        for b in range(0, 9):
            if(a == x and b != y):
                if len(board_b[a][b]) == 1:
                    if(board_b[x][y].__contains__(board_b[a][b][0])):
                        board_b[x][y].remove(board_b[a][b][0])
            if(b == y and a != x):
                if len(board_b[a][b]) == 1:
                    if(board_b[x][y].__contains__(board_b[a][b][0])):
                        board_b[x][y].remove(board_b[a][b][0])
            if((floor(y/3) + 3*floor(x/3)) == (floor(b/3) + 3*floor(a/3)) and (a != x and b != y)):
                if(len(board_b[a][b]) == 1):
                    if(board_b[x][y].__contains__(board_b[a][b][0])):
                        board_b[x][y].remove(board_b[a][b][0])
            

def reduceBoard_b():
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board_b[x][y]) > 1):
                reduceSpot_b(x, y)

def printBoard():
    for x in range(0, 9):
        rowToPrint = []
        for y in range(0, 9):
            if(len(board[x][y]) == 1):
                rowToPrint.append(board[x][y][0])
            else:
                rowToPrint.append(0)
        print(rowToPrint)

def countKnown():        
    count = 0
    for row in board:
        for col in row:
            if(len(col) == 1):
                count += 1
    return count

def countKnown_a():        
    count = 0
    for row in board_a:
        for col in row:
            if(len(col) == 1):
                count += 1
    return count

def countKnown_b():        
    count = 0
    for row in board_b:
        for col in row:
            if(len(col) == 1):
                count += 1
    return count


def reduceNeeds():
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board[x][y]) == 1):
                if rowNeeds[x].__contains__(board[x][y][0]):
                    rowNeeds[x].remove(board[x][y][0])
                if colNeeds[y].__contains__(board[x][y][0]):
                    colNeeds[y].remove(board[x][y][0])              
                if (sectorNeeds[floor(y/3) + (3 * floor(x/3))].__contains__(board[x][y][0])):
                    sectorNeeds[floor(y/3) + (3 * floor(x/3))].remove(board[x][y][0])


def fillRowNeeds():
    for x in range(0, 9):
        for num in rowNeeds[x]:
            count = 0
            xList = []
            yList = []
            for y in range(0, 9):
                if board[x][y].__contains__(num):
                    count += 1
                    xList.append(x)
                    yList.append(y)
            if count == 1:
                board[xList[0]][yList[0]] = [num]
                reduceNeeds()
                reduceBoard()
                print("Added:", num, "at row:", xList[0], "col:", yList[0])


def fillColNeeds():
    for y in range(0, 9):
        for num in colNeeds[y]:
            count = 0
            xList = []
            yList = []
            for x in range(0, 9):
                if board[x][y].__contains__(num):
                    count += 1
                    xList.append(x)
                    yList.append(y)
            if count == 1:
                board[xList[0]][yList[0]] = [num]
                reduceNeeds()
                reduceBoard()
                print("Added:", num, "at row:", xList[0], "col:", yList[0])


def fillSectorNeeds():
    for sector in range(0, 9):
        for num in sectorNeeds[sector]:
            count = 0
            xList = []
            yList = []
            for i in range(0, 9):
                x = floor(i/3) + 3*floor(sector/3)
                y = (i % 3) + 3*(sector % 3)
                if(board[x][y].__contains__(num)):
                    count += 1
                    xList.append(x)
                    yList.append(y)
            if count == 1:
                board[xList[0]][yList[0]] = [num]
                reduceNeeds()
                reduceBoard()
                print("Added:", num, "at row:", xList[0], "col:", yList[0])

def chainSolve():
    global board
    global board_a
    global board_b
    
    row = 0
    col = 0
    found = False
    option_a = 0
    option_b = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if((not found) and (len(board[x][y]) == 2)):
                found = True
                row = x
                col = y
                option_a = board[x][y][0]
                option_b = board[x][y][1]
    
    board_a = copy.deepcopy(board)
    board_b = copy.deepcopy(board)
    board_a[row][col] = [option_a]
    knownPrev_a = 0
    known_a = countKnown_a()
    while known_a != knownPrev_a:
        reduceBoard_a()
        knownPrev_a = known_a
        known_a = countKnown_a()
    
    board_b[row][col] = [option_b]
    knownPrev_b = 0
    known_b = countKnown_b()
    while known_b != knownPrev_b:
        reduceBoard_b()
        knownPrev_b = known_b
        known_b = countKnown_b()
    
    if(known_a == 81):
        board = board_a
    elif(known_b == 81):
        board = board_b
    else:
        print("Error: known_a =", known_a, " known_b =", known_b)

def solve():
    print("Original Board")
    print("Known Spots:", countKnown())
    printBoard()
    reduceNeeds()
    reduceBoard()
    knownPrev = 0
    known = countKnown()
    iterations = 0
    while known != knownPrev:
        fillRowNeeds()
        print("Fill Row Known", countKnown())
        fillColNeeds()
        print("Fill Col Known", countKnown())
        fillSectorNeeds()
        print("Fill Sector Known", countKnown())
        # print("Mistakes:", checkMistakes())
        
        printBoard()
        knownPrev = known
        known = countKnown()
        print("Known:", known)
        print("KnownPrev:", knownPrev)
        iterations = iterations + 1
        print("Iterations:", iterations)
    
    if countKnown() < 81:
        chainSolve()
        
    printBoard()
    for row in board:
        print(row)

solve()