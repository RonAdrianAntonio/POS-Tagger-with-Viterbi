import sys
from viterbi.viterbi import viterbi as vt


def main(transName, emiName, startProbName, posTagsName, symbolsName):
    viter = vt(transName, emiName, startProbName, posTagsName, symbolsName)

    print("Welcome to my Viterbi implementation!")
    while True:
        print("\n\nPlease type in 'exit' for the symbol sequence to exit out of the program.")
        print("Please enter the symbol sequence")
        observation = input()
        if observation == "exit":
            print("Thank you for using my Viterbi implementation!")
            return
        viter.run(observation)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
