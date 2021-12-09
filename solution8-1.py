def main():
    file = open('input8.txt', 'r')
    answer = 0
    lines = file.readlines()

    uniquesegments = [2,4,3,7]

    for line in lines:
        output = line.split(' | ')[1]
        output = output.split('\n')[0]
        output = output.split(' ')
        print(output)

        for digit in output:
            if len(digit) in uniquesegments:
                answer += 1
                print(digit)

    print(answer)

main()