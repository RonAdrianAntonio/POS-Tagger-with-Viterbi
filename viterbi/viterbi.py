import sys
class viterbi:
    
    transArr, emiArr, startArr, posArr, symArr = [], [], [], [], []


    def filesToArrays(self, transName, emiName, startProbName, posTagsName, symbolsName):

        with open(transName, 'r') as transFile:
            transArr = [[float(x) for x in line.split()] for line in transFile.read().split('\n') if len(line) > 0]

        with open(emiName, 'r') as emiFile:
            emiArr = [[float(x) for x in line.split()] for line in emiFile.read().split('\n') if len(line) > 0]
        
        with open(startProbName, 'r') as strtFile:
            startArr = [float(x) for x in strtFile.read().split()]

        with open(posTagsName, 'r') as posFile:
            posArr = ['NaN'] + [x for x in posFile.read().split()]

        with open(symbolsName, 'r') as symFile:
            symArr = [x for x in symFile.read().split()]

        return transArr, emiArr, startArr, posArr, symArr



    def __init__(self, transName, emiName, startProbName, posTagsName, symbolsName):


        self.transArr, self.emiArr, self.startArr, self.posArr, self.symArr = self.filesToArrays(transName, emiName, startProbName, posTagsName, symbolsName)

    def obvsStringToInt(self, observation):


        return [self.symArr.index(x) for x in [y for y in observation]]




    def run(self, obvsString):

        observation = obvsStringToInt(obvsString)

        viterbiArr = [[0.0 for symbol in range(len(self.transArr))] for state in range(len(observation))]
        viterbiMaxPrevState = [[-1 for symbol in range(len(self.transArr))] for state in range(len(observation))]

        for currIdx in range(len(viterbiArr)):
            if currIdx < 1:
                for currStateIdx in range(len(self.emiArr)):
                    print(self.emiArr)
                    print(self.startArr)
                    viterbiArr[currIdx][currStateIdx] = self.emiArr[currStateIdx][observation[currIdx]] * self.startArr[currStateIdx]
                    viterbiMaxPrevState[currIdx][currStateIdx] = 0
                #print(viterbiArr[0])
            else:
                for currStateIdx in range(len(self.emiArr)):
                    maxVal, maxIdx = getMaxState(viterbiArr[currIdx-1], self.transArr, currStateIdx)
                    viterbiArr[currIdx][currStateIdx] = self.emiArr[currStateIdx][observation[currIdx]] * maxVal
                    viterbiMaxPrevState[currIdx][currStateIdx] = maxIdx + 1


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
        
        for currPos in range(len(observation)-1, -1, -1):
            finalList.append(posArr[finalStateIdx])
            finalStateIdx = viterbiMaxPrevState[currPos][finalStateIdx -1]

        finalList.reverse()
                    

        print("\nFinal Result:")
        print(finalList)


    def getMaxState(self, row, transitions, currentState):
        maxVal = float('-inf')
        currMaxIdx = -1;
        for idx in range(len(row)):
            currentValue = row[idx] * transitions[idx][currentState]
            if currentValue > maxVal:
                maxVal = currentValue
                currMaxIdx = idx
        return maxVal, currMaxIdx



