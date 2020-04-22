import random

positions = ['1st', '2nd', '3rd', '4th','5th', '6th', '7th']

#run easy
def game(max_guess_trials, max_guess_val):
    answer = random.randint(1,max_guess_val)
    i=0
    print('There is a whole number between [1-%d], which I am keeping, If you guess it right after %d guesses, you win; otherwise you loose'%(max_guess_val,max_guess_trials))
    while i < max_guess_trials:
        #get users choice

        while True:
            try:
                guess =int(input("Make your %s guess, value must be between [1,%d]: "%(positions[i],max_guess_val)))
                break
            except Exception:
                print("\tA letter is an invalid input, Enter a number\n")
        

        #validating
        while (1 > guess) or (max_guess_val < guess):
            try:
                print("\n\tInvalid guess, the number is between [1 and %d]. Please try again\n"%max_guess_val)
                guess = int(input("Repeat your %s guess: "%(positions[i])))
            except:
                guess = -1

        #increment the guess
        i+=1

        #test for correctness
        if guess == answer:
            print("Hurray!!! You got it right after %d trials, the correct answer is: %d"%(i,answer))
            return True
        else:
            print("\tThat was Wrong!")     
    print("\t The right answer was: %d"%answer)
    return False

def intro_and_menu():
    out = "This game has three difficulty levels below\n"
    out+= "Enter the text in the <> brackets to select your difficulty\n\n"
    out+= "<EASY> The Easy level\n"
    out+= "<MED> The Medium level\n"
    out+= "<HARD> The Hard level\n"
    return out 





if __name__ == "__main__":
    
    #Initialize the screen
    print('********************************************************************')
    print('------------------------NUMBER GUESSING GAME------------------------')

    valid_entry = {'EASY':'Easy', 'MED':'Medium', 'HARD':'Hard'}
    
    print(intro_and_menu())
    raw= input('Select your Level: ')
    
    while not (raw.upper() in valid_entry):
        print("Invalid option, please try again")
        print("")
        print(intro_and_menu())
        raw = input("Once again, select a valid level: ")

    raw = raw.upper()
    max_trials = {'EASY':6, 'MED':4, 'HARD': 3}
    max_range = {'EASY':10, 'MED':20, 'HARD': 50}

    print('*************************************************************************')
    print('THE GAME STARTS NOW:\t\t\t DIFFICULTY: %s \n'%valid_entry[raw])
    win_out = game(max_trials[raw],max_range[raw])
    print()

    if win_out:
        print("YOU WIN - THE COMPUTER LOST")
    else:
        print("COMPUTER WIN - GAME OVER")
    print("*********************************************************************************")