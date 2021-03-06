import random

#Sets two variables, Slope and yIntercept, to be random numbers between 1 and 10
def setValues():
    gameCount = 0
    Slope = random.randint(1,10)
    yIntercept = random.randint(1,10)
    inputOutput(Slope, yIntercept, gameCount)

#Requests user input, and prompts the user when they try to inSeput non numerical value
def inputOutput(Slope, yIntercept, gameCount):
    x = raw_input("Please select a number: ")
    while x.isdigit() == False:
        x = raw_input("Only numbers please. Please select a number: ")

    #takes user input and plugs it into formula y = mx + b, then prints the y value and shows equation
    compRule = Slope*int(x)+yIntercept
    print 'm('+str(int(x))+')+'+'b= '+str(compRule)
    print ' '
    gameCount = gameCount + 1

    y = raw_input('Do you need another guess? Enter yes or no: ')
    y = y.lower()
    while y != 'yes' and y!= 'no':
        y = raw_input('Do you need another guess? Enter yes or no: ')


    if y == 'yes':
        inputOutput(Slope, yIntercept, gameCount)
    elif y == 'no':
        GuessRule(Slope, yIntercept, gameCount)
    return gameCount


#Asks user their guess for m, and if correct prompts the user for their guess for b,
#if not correct however, tells user they are incorrect and has them go back to plugging in values
def GuessRule(Slope, yIntercept, gameCount):
    z = raw_input('What do you think m is? ')
    while z.isdigit() == False:
        z = raw_input('m is an integer. What do you think m is? ')
    if int(z) == Slope:
        print 'Good job!'
        print ' '
        q = raw_input('What do you think b is? ')
        while q.isdigit() == False:
            q = raw_input('b is an integer. What do you think b is? ')
        if int(q) == yIntercept:
            print 'You win!'
            print ' '
            triesToPlayAgain(gameCount)
        else:
            print 'Nope'
            print 'Try more numbers'
            inputOutput(Slope, yIntercept, gameCount)

    else:
        print 'Nope'
        print 'Try more numbers'
        print ' '
        inputOutput(Slope, yIntercept, gameCount)

def triesToPlayAgain(gameCount):
    if gameCount == 1:
        print 'That took you ' + str(gameCount) + ' try!'
    else:
        print 'That took you ' + str(gameCount) + ' tries!'
    playAgain()

def  playAgain():
    print ' '
    m = raw_input('Would you like to play again? Enter yes or no: ')
    m = m.lower()
    if m == 'yes':
        setValues()
    elif m == 'no':
        print "Byebye!"
    while m != 'yes' and m!= 'no':
        raw_input('Would you like to play again? Enter yes or no: ')


#Explains instructions of game to user
def instructions():
    print "Hello, and welcome, to Guess My Rule Game!"
    print "I'm thinking of two numbers, each between 1 and 10"
    print "You give me a number, and i'll show you what my mystery function spits out"
    print "You try to guess my numbers."
    print "In this case, the mystery function is in the form y = mx+b."
    print "m and b are my numbers, while x is yours."
    print "When you think you know my numbers, tell me you don't need more guesses by typing 'no' and you can try to guess them."
    print " "

def main():
    instructions()
    setValues()

main()
