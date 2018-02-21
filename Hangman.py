import sys

def AskUserToGuessLetter():
    print ('Please guess a new letter')
    while True:
        userInput = input(':')
        if (len(userInput) == 1) and (not userInput.isdigit()):
            break
        print ('Please enter only one character that is not a number')
    return userInput.lower()
    

def DisplayHiddenWordWithCorrectlyGuessedLetters():
    print ('Guesses left : ' + str(MaxStrikes - Strikes) + '  Word to guess: ', end='')
    for i in range(len(WordToGuess)):
        if(LetterGuessed[i]):
            print(WordToGuess[i], end=' ')
        else:                       
            print('_', end=' ')
    print("")
    return

def CheckForLetter(letter):
    isLetter = False;
    for i in range(len(WordToGuess)):
        if(letter == WordToGuess[i]):
            LetterGuessed[i] = True
            isLetter = True

    if(not isLetter):    
        global Strikes
        Strikes += 1            
    return

def CheckIfUserWon():
    won = True
    for letter in LetterGuessed:
        if(not letter):
            won = False
    return won
        
def PrintWithWhiteSpace(outputString):
    print('\n\n\n')
    print(outputString)
    print('\n\n\n')

WordToGuess = "responsibilities"
GameOver = False
GameWon = False
Strikes = 0
MaxStrikes = 5


LetterGuessed = [False for i in range(len(WordToGuess))]

while(not GameOver and not GameWon):
    DisplayHiddenWordWithCorrectlyGuessedLetters()
    nextGuess = AskUserToGuessLetter()    
    CheckForLetter(nextGuess)
    GameWon = CheckIfUserWon()
    if(Strikes >= MaxStrikes):
        GameOver = True

if (GameOver):
    PrintWithWhiteSpace ('You have lost')

if (GameWon):    
    PrintWithWhiteSpace ('Congradulations, you have won!')

print ('The word was: '+WordToGuess)
sys.exit()
