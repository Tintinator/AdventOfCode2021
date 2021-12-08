import sys

def main():
    file = open('input7.txt', 'r')

    answer = -1

    input = file.readline()
    input = input.split(',')
    input = [int(x) for x in input]

    maxDist = input[0]

    dp = []
    dp.append(0)

    inputfreq = {}
    for x in input:
        maxDist = max(x, maxDist)
        dp[0]+= x
        inputfreq[x] = inputfreq.get(x,0) + 1

    crabsAboveCurrentPosition = 0
    crabsBelowCurrentPosition = 0
    for x in inputfreq.keys():
        if x >= 0:
            crabsAboveCurrentPosition += inputfreq[x]

    for position in range(1, maxDist+1):
        # print("Cost for position " + str(position) + ": " + str(dp[position-1]))

        previousCost = dp[position-1]
        crabsBelowCurrentPosition += inputfreq.get(position-1, 0)
        crabsAboveCurrentPosition -= inputfreq.get(position-1, 0)
        cost = previousCost + crabsBelowCurrentPosition - crabsAboveCurrentPosition

        dp.append(cost)
        answer = cost if answer == -1 else min(answer, cost)
        pass

    print(answer)

main()