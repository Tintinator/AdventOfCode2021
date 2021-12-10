def isLow(row, col, input):

    row_bound = len(input)
    col_bound = len(input[0])

    if row -1 > -1:
        if input[row-1][col] <= input[row][col]:
            return False

    if row + 1 < row_bound:
        if input[row+1][col] <= input[row][col]:
            return False

    if col - 1 > -1:
        if input[row][col-1] <= input[row][col]:
            return False

    if col + 1 < col_bound:
        if input[row][col+1] <= input[row][col]:
            return False

    return True

def main():
    file = open('input9.txt', 'r')
    file = file.readlines()
    answer = 0
    input = []

    # parse input
    for line in file:
        curline = line.split('\n')[0]
        curline = list(curline)
        curline = [int(elem) for elem in curline]
        input.append(curline)

    for x in range(0, len(input)):
        for y in range(0, len(input[0])):
            if isLow(x,y, input):
                print('Low Point:', input[x][y])
                answer += (1 + input[x][y])

    
    print(answer)

main()