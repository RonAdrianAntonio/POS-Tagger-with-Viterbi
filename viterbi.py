import sys
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

def main(transName, emiName, startProbName, posTagsName):
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
    with open(posTagsName, 'r') as posFile:
        posArr = ['NaN'] + [x for x in posFile.read().split()]


    viterbiArr = [[0.0 for symbol in range(len(transArr))] for state in range(len(OBVS))]
    viterbiMaxPrevState = [[-1 for symbol in range(len(transArr))] for state in range(len(OBVS))]

    for currIdx in range(len(viterbiArr)):
        if currIdx < 1:
            for currStateIdx in range(len(emiArr)):
                viterbiArr[currIdx][currStateIdx] = emiArr[currStateIdx][OBVS[currIdx]] * startArr[currStateIdx]
                viterbiMaxPrevState[currIdx][currStateIdx] = 0
            #print(viterbiArr[0])
        else:
            for currStateIdx in range(len(emiArr)):
                maxVal, maxIdx = getMaxState(viterbiArr[currIdx-1], transArr, currStateIdx)
                viterbiArr[currIdx][currStateIdx] = emiArr[currStateIdx][OBVS[currIdx]] * maxVal
                viterbiMaxPrevState[currIdx][currStateIdx] = maxIdx + 1#'y'+str(maxIdx+1)

    print("Table:")
    for x in viterbiArr:
        print(x)
    
    
    print("\nSymbols:")
    for x in viterbiMaxPrevState:
        print([posArr[y] for y in x])

    print("\nSymbol Idx:")
    for x in viterbiMaxPrevState:
        print([y for y in x])

    finalList = []
    finalStateSigma = viterbiArr[len(viterbiMaxPrevState)-1]
    finalStateIdx = finalStateSigma.index(max(finalStateSigma))+1
    
    for currPos in range(len(OBVS)-1, -1, -1):
        finalList.append(posArr[finalStateIdx])
        finalStateIdx = viterbiMaxPrevState[currPos][finalStateIdx -1]

    finalList.reverse()
                

    print("\nFinal Result:")
    print(finalList)



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
