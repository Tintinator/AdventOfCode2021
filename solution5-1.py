import sys

def main():
    res = 0
    freq = {}
    file = open('input5.txt', 'r')

    for line in file.readlines():
        input = line.split(' -> ')
        point1 = input[0].split(',')
        point2 = input[1].split(',')
        x1,y1 = [int(x) for x in point1]
        x2,y2 = [int(x) for x in point2]

        if x1 == x2:
            low = min([y1, y2])
            high = max([y1, y2])
            
            for x in range(low, high+1):
                key = str(x1) + "," + str(x)
                freq[key] = freq.get(key, 0)+1
                

        elif y1 == y2:
            low = min([x1, x2])
            high = max([x1, x2])
            
            for x in range(low, high+1):
                key = str(x) + "," + str(y1)
                freq[key] = freq.get(key, 0)+1

        elif abs((x1-x2)/(y1-y2)) == 1:
            print('DIAGONAL: ', point1, ' AND', point2)
            leftpoint, rightpoint = [[x1, y1], [x2, y2]] if (x1 < x2) else [[x2, y2], [x1, y1]]
            incrementer = 1 if (leftpoint[1] < rightpoint[1]) else -1
            height = leftpoint[1]

            for x in range(leftpoint[0], rightpoint[0]+1):
                key = str(x) + ',' + str(height)
                freq[key] = freq.get(key, 0)+1
                height += incrementer

    for value in freq.values():
        if value > 1:
            res+=1

    print(res)

main()