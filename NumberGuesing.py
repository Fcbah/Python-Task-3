import random

positions = ['1st', '2nd', '3rd', '4th','5th', '6th', '7th']

#run easy
def game(max_guess_trials, max_guess_val):
    answer = random.randint(1,max_guess_val)
    i=0
    print('There is a whole number between [1-%d], which I am keeping, If you guess it right after %d guesses, you win; otherwise you loose'%(max_guess_val,max_guess_trials))
    while i < max_guess_trials:
        #get users choice
        guess =int(input("Make your %s guess, value must be between [1,%d]: "%(positions[i],max_guess_val)))

        #validating
        while (1 > guess) or (max_guess_val < guess):
            print("Invalid guess, the number is between [1 and %d]. Please try again"%max_guess_val)
            guess = int(input("Repeat your %s guess: "%(positions[i])))

        #increment the guess
        i+=1

        #test for correctness
        if guess == answer:
            print("Hurray!!! You got it right after %d trials, the correct answer is: %d"%(i,answer))
            return True
        
    
    return False



if __name__ == "__main__":
    
    #Initialize the screen
    print('********************************************************************')
    print('------------------------NUMBER GUESSING GAME------------------------')

    #Get input on the difficulty
    input("")