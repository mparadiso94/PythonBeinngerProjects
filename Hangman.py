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
        if(LetterGuessedBools[i]):
            print(WordToGuess[i], end=' ')
        else:                       
            print('_', end=' ')
    print("")
    return

def CheckForLetter(letter):    
    global LettersGuessed
    global Strikes
    
    isLetter = False;
    
    for c in LettersGuessed:
        if(letter == c):
            print('You have already guessed the letter ' + letter + '!')
            return
    
    for i in range(len(WordToGuess)):
        if(letter == WordToGuess[i]):
            LetterGuessedBools[i] = True
            isLetter = True   

    if(not isLetter):              
        Strikes += 1
    
    LettersGuessed += letter  
    return

def CheckIfUserWon():
    won = True
    for letter in LetterGuessedBools:
        if(not letter):
            won = False
    return won
        
def PrintWithWhiteSpace(outputString):
    print('\n\n\n')
    print(outputString)
    print('\n\n\n')

def DisplayLettersGuessed():
    print ('Letters guessed:', end=' ')
    for c in LettersGuessed:        
        print(c, end=' ')
    print('')
    return

WordToGuess = "responsibilities"
GameOver = False
GameWon = False
Strikes = 0
MaxStrikes = 5
LettersGuessed = ''

LetterGuessedBools = [False for i in range(len(WordToGuess))]

while(not GameOver and not GameWon):
    PrintWithWhiteSpace('')
    DisplayHiddenWordWithCorrectlyGuessedLetters()
    DisplayLettersGuessed()
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
