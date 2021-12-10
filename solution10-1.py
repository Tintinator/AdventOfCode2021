def main():
    file = open('input10.txt', 'r')
    file = file.readlines()
    answer = 0

    openclose = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }
    closeopen = {value : key for (key, value) in openclose.items()}

    illegalvalue = {
        '}': 1197,
        ']': 57,
        ')': 3,
        '>': 25137
    }
    
    for line in file:
        array = []

        for x in line:
            if x in openclose:
                array.append(x)
            elif x in closeopen:
                opener = array.pop()
                if opener != closeopen[x]:
                    answer += illegalvalue[x]
                    break

    print(answer)
    
main()