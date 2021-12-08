import sys

def main():
    file = open('input6.txt', 'r')
    input = file.readline()
    input = input.split(',')
    input = [int(x) for x in input]
    answer = 0

    fishfreq = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

    for fish in input:
        fishfreq[fish] = fishfreq[fish]+1

    for day in range(0,256):
        
        #dict swap
        fishfreq[8], fishfreq[7], fishfreq[6], fishfreq[5], fishfreq[4], fishfreq[3], fishfreq[2], fishfreq[1], fishfreq[0] = \
        fishfreq[0], fishfreq[8], fishfreq[7] + fishfreq[0], fishfreq[6], fishfreq[5], fishfreq[4], fishfreq[3], fishfreq[2], fishfreq[1]

    for x in fishfreq.values():
        answer += x

    print(answer)

main()