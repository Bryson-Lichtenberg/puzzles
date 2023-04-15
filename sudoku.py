from math import floor

board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [1, 2, 3, 4, 5, 6, 7, 8, 9], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3]],
         [[1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
         [[1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8]],
         [[2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [6], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

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

def checkMistakes():
    mistakes = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if len(board[x][y]) == 1:
                if board[x][y][0] != solved[x][y]:
                    mistakes += 1
    return mistakes


# TEST -------------------------------------------------------------------------------------
def reduceNeeds():
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
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board[x][y]) == 1):
                if rowNeeds[x].__contains__(board[x][y][0]):
                    rowNeeds[x].remove(board[x][y][0])
                if colNeeds[y].__contains__(board[x][y][0]):
                    colNeeds[y].remove(board[x][y][0])
                if (sectorNeeds[floor(x/3) + (3 * floor(y/3))].__contains__(board[x][y][0])):
                    sectorNeeds[floor(x/3) + (3 * floor(y/3))].remove(board[x][y][0])



def fillRowNeeds():
    for x in range(0, 9):
        for num in rowNeeds[x]:
            count = 0
            for y in range(0, 9):
                if(board[x][y].__contains__(num)):
                    count += 1
            if count == 1:
                for y in range(0, 9):
                    if(board[x][y].__contains__(num)):
                        board[x][y] = [num]
                        print("Fill Row ADDED: num, x, y")
                        
                        print(num)
                        print(x)
                        print(y)
                        if solved[x][y] != num:
                            print("ERROR in fillRow: x, y, inserted, actual")
                            print(x)
                            print(y)
                            print(num)
                            print(solved[x][y])

                        # print("ROW NUM CHANGED___________________________________________________________")

def fillColNeeds():
    # print("colNeeds")
    # print(colNeeds)
    for y in range(0, 9):
        # print("COLUMN: " + str(y))
        # print(colNeeds[y])
        for num in colNeeds[y]:
            count = 0
            # print("col: " + str(y))
            # print("Num: " + str(num))
            for x in range(0, 9):
                if(board[x][y].__contains__(num)):
                    count += 1
            # print("count: " + str(count))
            if count == 1:
                for x in range(0, 9):
                    if(board[x][y].__contains__(num)):
                        board[x][y] = [num]
                        print("Fill Col ADDED: num, x, y")
                        
                        print(num)
                        print(x)
                        print(y)
                        if solved[x][y] != num:
                            print("ERROR in fillCol: x, y, inserted, actual")
                            print(x)
                            print(y)
                            print(num)
                            print(solved[x][y])
                        # print("COL NUM CHANGED___________________________________________________________")

def fillSectorNeeds():
    for sector in range(0, 9):
        for num in sectorNeeds[sector]:
            count = 0
            for i in range(0, 9):
                x = floor(i/3)
                y = i % 3
                if(board[x][y].__contains__(num)):
                        count += 1
            if count == 1:
                for i in range(0, 9):
                    x = floor(i/3)
                    y = i % 3
                    if(board[x][y].__contains__(num)):
                        board[x][y] = [num]
                        print("Fill Sector ADDED: num, x, y")
                        
                        print(num)
                        print(x)
                        print(y)
                        if solved[x][y] != num:
                            print("ERROR in fillSector: x, y, inserted, actual")
                            print(x)
                            print(y)
                            print(num)
                            print(solved[x][y])
                        # print("SECTOR NUM CHANGED___________________________________________________________")



def fillBoard():
    
    reduceNeeds()
    fillRowNeeds()  
    print("Mistakes: fillRow")
    print(checkMistakes())
    reduceNeeds()
    fillColNeeds()  
    print("Mistakes: fillCol")
    print(checkMistakes())
    reduceNeeds()
    fillSectorNeeds()  
    print("Mistakes: fillSector")
    print(checkMistakes())




def countKnown():        
    count = 0
    for row in board:
        for col in row:
            if(len(col) == 1):
                count += 1
    return count


print("Number of Spots known")
print(countKnown())

def reduceSpot(x, y):
    for a in range(0, 9):
        for b in range(0, 9):
            if(a == x):
                if len(board[a][b]) == 1:
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            if(b == y):
                if len(board[a][b]) == 1:
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            if(floor(x/3) == floor(a/3) and (floor(y/3) == floor(b/3))):
                if(len(board[a][b]) == 1):
                    if(board[x][y].__contains__(board[a][b][0])):
                        board[x][y].remove(board[a][b][0])
            


def reduceBoard():
    for x in range(0, 9):
        for y in range(0, 9):
            if(len(board[x][y]) > 1):
                reduceSpot(x, y)
            


# print(board)
def printBoard():
    for x in range(0, 9):
        rowToPrint = []
        for y in range(0, 9):
            if(len(board[x][y]) == 1):
                rowToPrint.append(board[x][y][0])
            else:
                rowToPrint.append(0)
        print(rowToPrint)

printBoard()
for num in range(0, 1):
    reduceBoard()
    
    print("Reduce: Number of Spots known")
    print(countKnown())  
    printBoard() 
    print("Mistakes: ")
    print(checkMistakes())

    # print("messy board")
    # print(board)

    
    fillBoard()
    print("Fill: Number of Spots known")
    print(countKnown())
    printBoard()  

# RUN IN RANGE (0, 4)
# Sector 6 mixes up 8 and 4...



#      y   y   y    y   y   y    y   y   y
# x  0,0 0,1 0,2  0,3 0,4 0,5  0,6 0,7 0,8
# x  1,0 1,1 1,2  1,3 1,4 1,5  1,6 1,7 1,8
# x  2,0 2,1 2,2  2,4 2,4 2,5  2,6 2,7 2,8

# x  3,0 3,1 3,2  3,3 3,4 3,5  3,6 3,7 3,8
# x  4,0 4,1 4,2  4,3 4,4 4,5  4,6 4,7 4,8
# x  5,0 5,1 5,2  5,3 5,4 5,5  5,6 5,7 5,8

# x  6,0 6,1 6,2  6,3 6,4 6,5  6,6 6,7 6,8
# x  7,0 7,1 7,2  7,3 7,4 7,5  7,6 7,7 7,8
# x  8,0 8,1 8,2  8,3 8,4 8,5  8,6 8,7 8,8

