import sys
from viterbi.viterbi import viterbi as vt


def main(transName, emiName, startProbName, posTagsName, symbolsName):
    print("Please enter the symbol sequence")
    observation = input()

    viter = vt(transName, emiName, startProbName, posTagsName, symbolsName)

    viter.run(observation)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
