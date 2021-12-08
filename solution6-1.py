def main():
    file = open('input6.txt', 'r')
    input = file.readline()
    input = input.split(',')
    input = [int(x) for x in input]
    
    for x in range(0, 80):
        for fishidx in range(0, len(input)):
            curfish = input[fishidx]
            if curfish == 0:
                input.append(8)
                input[fishidx] = 6
            else:
                input[fishidx] = curfish-1

    print(len(input))


main()