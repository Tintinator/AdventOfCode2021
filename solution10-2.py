def main():
    file = open('input10.txt', 'r')
    file = file.readlines()
    illegalscore = 0
    incompletescore = []

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

    incompletevalue = {
        '}': 3,
        ']': 2,
        ')': 1,
        '>': 4
    }
    
    for line in file:
        array = []
        isIncomplete = True

        for x in line:
            if x in openclose:
                array.append(x)
            elif x in closeopen:
                opener = array.pop()
                if opener != closeopen[x]:
                    illegalscore += illegalvalue[x]
                    isIncomplete = False
                    break

        if isIncomplete:
            incompletecost = 0
            array.reverse()
            for x in array:
                incompletecost = (5*incompletecost) + incompletevalue[openclose[x]]
            incompletescore.append(incompletecost)

            
    incompletescore.sort()
    print(illegalscore)
    print(incompletescore[len(incompletescore)/2])
    
main()