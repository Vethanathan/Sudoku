def loadPuzzle():
    board = []
    fileHandle = open("SudokuPuzzle.txt", "r")
    puzzle = fileHandle.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
            board.append(list(map(str, puzzle[line])))
        else:
            board.append(list(map(str, puzzle[line])))
    fileHandle.close()
    return board


def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True

            grid[i][j] = 0
    return False


def issolvable(question, solution):
    if question == solution:
        return True
    else:
        return False


def printBoard(board):
    for i in range(9):
        for j in range(9):
            board[i][j] = int(board[i][j])
    for i in board:
        print(*i)


board = loadPuzzle()
board[-1] = board[-1][:-1]

q = [[0] * 9 for i in range(9)]
for i in range(9):
    for j in range(9):
        q[i][j] = board[i][j]

if issolvable(q, board):
    print("Unsolvable")
else:
    print("\n Initial board:\n")
    printBoard(board)

    solveSudoku(board)

    print("\noutput:\n")
    printBoard(board)
