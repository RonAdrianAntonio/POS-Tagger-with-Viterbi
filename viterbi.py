import sys
NUMBER_OF_OBVS = 5
#below is just number of symbol emitted-1, since this is
#how it's stored in an array
OBVS = [0, 3, 1, 1, 3]
def getMaxState(row, transitions, currentState):
    maxVal = float('-inf')
    currMaxIdx = -1;
    for idx in range(len(row)):
        currentValue = row[idx] * transitions[idx][currentState]
        if currentValue > maxVal:
            maxVal = currentValue
            currMaxIdx = idx
    return maxVal, currMaxIdx

def main(transName, emiName, startProbName):
    with open(transName, 'r') as transFile:
        transArr = [[float(x) for x in line.split()] for line in transFile.read().split('\n') if len(line) > 0]
    #for x in transArr:
    #    print(x)

    with open(emiName, 'r') as emiFile:
        emiArr = [[float(x) for x in line.split()] for line in emiFile.read().split('\n') if len(line) > 0]
    #for x in emiArr:
    #    print(x)
    
    with open(startProbName, 'r') as strtFile:
        startArr = [float(x) for x in strtFile.read().split()]
    #for x in startArr:
    #    print(x)


    viterbiArr = [[0.0 for symbol in range(len(transArr))] for state in range(NUMBER_OF_OBVS)]
    viterbiMaxPrevState = [['' for symbol in range(len(transArr))] for state in range(NUMBER_OF_OBVS)]

    for currIdx in range(len(viterbiArr)):
        if currIdx < 1:
            for currStateIdx in range(len(emiArr)):
                viterbiArr[currIdx][currStateIdx] = emiArr[currStateIdx][OBVS[currIdx]] * startArr[currStateIdx]
                viterbiMaxPrevState[currIdx][currStateIdx] = 'NaN'
            #print(viterbiArr[0])
        else:
            for currStateIdx in range(len(emiArr)):
                maxVal, maxIdx = getMaxState(viterbiArr[currIdx-1], transArr, currStateIdx)
                viterbiArr[currIdx][currStateIdx] = emiArr[currStateIdx][OBVS[currIdx]] * maxVal
                viterbiMaxPrevState[currIdx][currStateIdx] = 'y'+str(maxIdx+1)

    for x in viterbiArr:
        print(x)
                

    for x in viterbiMaxPrevState:
        print(x)

                


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
