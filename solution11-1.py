def valid(r, c):
    return r >= 0 and r < 10 and c >= 0 and c < 10


def incrementgrid(g):
    for x in range(0, 10):
        for y in range(0, 10):
            g[x][y] += 1


def process_flashes(g, d, r, c):
    flag = False

    for dir in d:
        new_r = r + dir[0]
        new_c = c + dir[1]
        if valid(new_r, new_c) and g[new_r][new_c] < 10 and g[new_r][new_c] >= 0:
            g[new_r][new_c] += 1
            if g[new_r][new_c] == 10:
                flag = True

    return flag


def process_input(g, directions):
    answer = 0
    flag = False

    for r in range(0, 10):
        for c in range(0, 10):
            if g[r][c] == 10:
                answer += 1
                g[r][c] = -1

    for r in range(0, 10):
        for c in range(0, 10):
            if g[r][c] == -1:
                if process_flashes(g, directions, r, c):
                    flag = True
                g[r][c] = -2

    # check for new flashes
    if flag:
        return answer + process_input(g, directions)

    return answer


def main():
    file = open("input11.txt", "r")
    file = file.readlines()
    input = []
    answer = 0

    directions = [[1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1]]

    # parse input
    for line in file:
        row = line.split("\n")[0]
        row = list(row)
        row = [int(x) for x in row]
        input.append(row)

    for x in range(1, 5000):
        # increment one
        incrementgrid(input)

        # process results
        answer += process_input(input, directions)

        # cleanie boy
        for r in range(0, 10):
            for c in range(0, 10):
                if input[r][c] == -2:
                    cleancount += 1
                    input[r][c] = 0

    print(answer)


main()
