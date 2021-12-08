def main():
    file = open('input7.txt', 'r')
    input = file.readline()
    input = input.split(',')
    input = [int(x) for x in input]
    answer = -1
    inputfreq = {}

    maxDist = input[0]
    for x in input:
        maxDist = max(x, maxDist)
        inputfreq[x] = inputfreq.get(x,0) + 1

    dist = []
    dist.append(0)
    for x in range(1, maxDist+1):
        dist.append(dist[x-1]+x)

    dp = []
    dp.append(0)
    for x in inputfreq.keys():
        dp[0] += inputfreq[x] * dist[x]

    for position in range(1, maxDist+1):
        crabsAboveCurrentPosition= sum([(dist[elem-(position-1)]-dist[elem-position])*inputfreq[elem] for elem in inputfreq.keys() if elem >= position])
        crabsBelowCurrentPosition = sum([(position-elem)*inputfreq[elem] for elem in inputfreq.keys() if elem < position])

        previousCost = dp[position-1]
        cost = previousCost - crabsAboveCurrentPosition + crabsBelowCurrentPosition 

        dp.append(cost)
        answer = cost if answer == -1 else min(answer, cost)
        pass

    print(answer)

main()