import random

hangManLayout = ["------\n|  |\n|\n|\n|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|\n|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|    |\n|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|   -|\n|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|   -|-\n|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|   -|-\n|    |\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|   -|-\n|   _|\n|\n|\n|\n|\n----------",
                 "------\n|    |\n|    0\n|   -|-\n|   _|_\n|\n|\n|\n|\n----------"]

wordsToGuess= ["cow", "bull", "chicken", "pig", "puppy", "goat", "donkey", "horse", "turkey", "rabbit", "alpaca",\
               "kitten", "goose"]

def chooseRandomWord(listOfWords):
    chosenWord = random.choice(listOfWords)
    return chosenWord

def displayState(stateNr):
    print(hangManLayout(stateNr))
    return

def processInput():
    letter = input("Please enter a letter\n").lower()
    if not letter.isalpha():
        print("That's not a letter, please try again\n")
        return processInput()
    elif len(letter) != 1:
        print("Please enter only one letter!\n")
        return processInput()
    return letter

def newGame():
    playGame = True
    attempts = 7
    i=0
    j=0
    wrongLetters = []
    wrongCounter = 0
    word = chooseRandomWord(wordsToGuess)
    wordCount = len(word)
    blankWord = '_' * wordCount
    print("Your random word has %d letters\n"%wordCount)
    for letter in blankWord:
        print(letter, end=' ')
    print("")

    while playGame:
        if len(wrongLetters) == len(hangManLayout):
            print("Sorry, you lost the game :(\n")
            print("The chosen word was %s" % (word))
            print("")
            return main()
        playerInput = processInput()
        if playerInput in wrongLetters:
            print("You already guessed that letter!\n")
            processInput()

        if playerInput in word:
            for i in range(wordCount):
                if word[i] in playerInput:
                    blankWord = blankWord[:i]+word[i]+blankWord[i+1:]

            for letter in blankWord:
                print(letter, end=' ')
            print("")
            if (blankWord==word):
                print("Well done! You have found the word!\n")
                print("------------------------------------\n")
                return main()
        else:
            wrongLetters.append(playerInput)
            print("Oops! You have %d attemps remaining\n" % attempts)
            print(hangManLayout[j])
            print("")
            print(wrongLetters)
            for letter in blankWord:
                print(letter, end=' ')
            print("")
            attempts= attempts-1
            j = j+1


def main():
    print("Welcome to Hangman: Farm animals!\n")
    answer= input("Do you wanna start a game?(yes/no)\n")
    if (answer=="yes"):
        newGame()
        return main()
    elif (answer == "no"):
        return
    else:
        print("That's not a correct answer!")
        return main()


if __name__=="__main__":
    main()