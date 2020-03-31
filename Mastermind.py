import random
legalcolours = ['r','o','y','g','b','v'] #list of legal colours
max_guess = 10 #number of allowed guess
numguess = 4 #number of guess each player has to make at every try

def generatePattern():
    pattern = random.choices(legalcolours, k=4)
    return pattern

def cleanGuess(guess):
    guess = guess.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for v in guess:
        if v not in alpha:
            guess = guess.replace(v,'')

    cleaned_guess = list(guess)
    return cleaned_guess

def guessIsValid(cleaned_guess):
    count = 0
    for color in cleaned_guess:
        if color in legalcolours:
            count += 1

    if count == numguess and len(cleaned_guess) == numguess:
        return True

    else:
        return False

def evaluateGuess(pattern,cleaned_guess):
    correct = 0
    position = 0
    temppattern = [val for val in pattern]
    tempguess = [guess for guess in cleaned_guess]

    for index,value in enumerate(tempguess):
        for ind,val in enumerate(temppattern):
            if ind == index and value == val:
                temppattern[ind] = 'x'
                tempguess[index] = 'x'
                correct += 1

    for ind,guess in enumerate(tempguess):
        if guess == 'x':
            continue

        elif guess in temppattern:
            tempguess[ind] = 'x'
            position += 1

    print(correct, 'correct colour in right position')
    print(position, 'correct colour in wrong position')

    return([correct,position])

def playGame():
    answer = [4,0] #correct pattern returns this result in evaluateGuess
    chance = 0 #counter for number of tries
    pattern = generatePattern()

    while chance < max_guess: #max number of tries
        guess = input('Enter your 4 guesses: ')
        cleaned_guess = cleanGuess(guess)

        if guessIsValid(cleaned_guess):
            result = evaluateGuess(cleaned_guess,pattern)

            if result == answer:
                print('Congratulations, you won! You have made {} guesses. My pattern was {}'.format(chance,pattern))
                return(chance)

            else:
                chance += 1

                if chance == max_guess:
                    print('You lost! You have made the maximum of {} guesses. My pattern was {}'.format(chance,pattern))
                    return(chance)

        else:
            print('you have entered an invalid guess. Please enter a new guesses')



if __name__ == '__main__':
    guesses = playGame()
    print('Game over after {} guesses'.format(guesses))

