import sys

winConditions = {
    1: [1,2,3,4,5],
    2: [6,7,8,9,10],
    3: [11,12,13,14,15],
    4: [16,17,18,19,20],
    5: [21,22,23,24,25],
    6: [1,6,11,16,21],
    7: [2,7,12,17,22],
    8: [3,8,13,18,23],
    9: [4,9,14,19,24],
    10: [5,10,15,20,25]
}

# add the values up. if it's -5, it's a win
def isWin(board):
    linesums = set()

    for line in winConditions.values():
        ls = 0
        for x in line:
            ls += board[x]
        linesums.add(ls)

    if -5 in linesums:
        return True

    return False

def main():
    
    recordTurns = -1
    recordScore = 0

    file = open('input4.txt', 'r')

    bingoInput = file.readline()
    line = file.readline()
    bingoInput = bingoInput.split(',')

    line = file.readline()
    
    while line:
        board = {}
        idxboard = {}
        boardsum = 0
        idx = 1

        # load board in dict
        # load values into a indexer
        for x in range(0,5):
            line = line.split(' ')
            
            for num in line:
                if num == '':
                    continue

                value = int(num)

                board[idx] = value
                idxboard[value] = idx
                boardsum += value
                idx+=1

            line = file.readline()
    
        # play board
        for i in range(0, len(bingoInput)):
            currentValue = int(bingoInput[i])

            if currentValue not in idxboard:
                continue
            
            boardsum -= currentValue
            boardIndex = idxboard[currentValue]
            board[boardIndex] = -1

            test = isWin(board)

            # if it wins
            if isWin(board):

                if i > recordTurns:
                    recordTurns = i
                    recordScore = currentValue * boardsum
                break
        
        line = file.readline()

    # print(recordTurns)
    # print(recordScore)

main()