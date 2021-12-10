def isInBound(row, col, input):

    row_bound = len(input)
    col_bound = len(input[0])

    return row >= 0 and row < row_bound and col >= 0 and col < col_bound and input[row][col] != 9

def dfs(r, c, input):
    if not isInBound(r,c, input):
        return 0
    
    input[r][c] = 9
    answer = 1 + dfs(r+1, c, input) + dfs(r-1, c, input) + dfs(r, c-1, input) + dfs(r, c+1, input)

    return answer

def main():
    file = open('input9.txt', 'r')
    file = file.readlines()
    answer = 0
    areas = []
    input = []

    # parse input
    for line in file:
        curline = line.split('\n')[0]
        curline = list(curline)
        curline = [int(elem) for elem in curline]
        input.append(curline)

    for x in range(0, len(input)):
        for y in range(0, len(input[0])):
            if input[x][y] == 9:
                continue
            else:
                areas.append(dfs(x, y, input))


    areas.sort()
    print(areas)
    print(areas[len(areas)-1] * areas[len(areas)-2] * areas[len(areas)-3])

main()