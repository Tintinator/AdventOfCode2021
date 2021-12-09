def sort(string):
    sorted_characters = sorted(string)
    return "".join(sorted_characters)

def finduniquenumbers(leftinput):
    numbermap = {}

    for x in leftinput:
        length = len(x)

        if length == 2:
            numbermap[1] = x
        elif length == 4:
            numbermap[4] = x
        elif length == 3:
            numbermap[7] = x
        elif length == 7:
            numbermap[8] = x

    return numbermap

def findtopsegment(one, seven):
    oneset = set(one)
    sevenset = set(seven)

    difference = oneset.symmetric_difference(sevenset)
    return list(difference)[0]

def findbotsegment(four, top, leftinput, numbermap):
    base = list(four)
    base.append(top)

    for x in leftinput:
        if len(x) == 6:
            result = list(set(x) - set(base))
            if len(result) == 1:
                numbermap[9] = x
                return result[0]

def findmidsegment(one, top, bot, leftinput, numbermap):
    base = list(one)
    base.append(top)
    base.append(bot)

    for x in leftinput:
        if len(x) == 5:
            result = list(set(x) - set(base))
            if len(result) == 1:
                numbermap[3] = x
                return result[0]

def findtlsegment(one, four, mid):
    fourset = set(four)
    oneset = set(one)
    oneset.add(mid)
    return list(fourset-oneset)[0]

def findbrsegment(brstring, leftinput, numbermap):
    stringset = set(brstring)

    for x in leftinput:
        if len(x) == 5:
            result = list(set(x) - stringset)
            if len(result) == 1:
                numbermap[5] = x
                return result[0]

def main():
    file = open('input8.txt', 'r')
    answer = 0
    lines = file.readlines()

    for line in lines:

        # parse input
        leftinput, rightinput = line.split(' | ')
        leftinput = leftinput.split(' ')
        leftinput = [sort(elem) for elem in leftinput]
        rightinput = rightinput.split('\n')[0]
        rightinput = rightinput.split(' ')
        rightinput = [sort(elem) for elem in rightinput]
        segmentmap = {}
        numbermap = finduniquenumbers(leftinput)

        # print
        # print(rightinput)

        # find TOP
        segmentmap['top'] = findtopsegment(numbermap[1], numbermap[7])
        # print('top: ', segmentmap['top'])

        # find 9 + BOT
        segmentmap['bot'] = findbotsegment(numbermap[4], segmentmap['top'], leftinput, numbermap)
        # print(numbermap[9])
        # print('bot: ', segmentmap['bot'])
        
        # find 3 + MIDDLE
        segmentmap['mid'] = findmidsegment(numbermap[1], segmentmap['top'], segmentmap['bot'], leftinput, numbermap)
        # print(numbermap[3])
        # print('mid: ', segmentmap['mid'])

        # find TOP LEFT 
        segmentmap['tl'] = findtlsegment(numbermap[1], numbermap[4], segmentmap['mid'])
        # print('tl: ', segmentmap['tl'])

        # find 5 + BOT RIGHT
        brstring = segmentmap['top'] + segmentmap['mid'] + segmentmap['bot'] + segmentmap['tl']
        segmentmap['br'] = findbrsegment(brstring, leftinput, numbermap)
        # print('br: ', segmentmap['br'])

        # find TOP RIGHT
        segmentmap['tr'] = list(set(numbermap[9])-set(numbermap[5]))[0]
        # print('tr: ', segmentmap['tr'])

        # find BOT LEFT
        segmentmap['bl'] = list(set(numbermap[8])-set(numbermap[9]))[0]
        # print('bl: ', segmentmap['bl'])

        # craft 0
        zero = [elem for elem in numbermap[8] if elem != segmentmap['mid']]
        zero = sort(zero)
        numbermap[0] = zero
        # print('zero: ', zero)

        # craft 2
        two = [elem for elem in numbermap[8] if elem not in [segmentmap['tl'], segmentmap['br']]]
        two = sort(two)
        numbermap[2] = two
        # print('two: ', two)

        # craft 6
        six = [elem for elem in numbermap[8] if elem != segmentmap['tr']]
        six = sort(six)
        numbermap[6] = six
        # print('six: ', six)

        reverse_numbermap = {value : key for (key, value) in numbermap.items()}

        resultnumber = ""
        for num in rightinput:
            resultnumber += str(reverse_numbermap[num])

        answer += int(resultnumber)

        

    print(answer)

main()