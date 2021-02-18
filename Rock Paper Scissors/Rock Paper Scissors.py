'''
Description: Player will play a game of rock paper scissors vs a computer.
The player can go on for as long as he/she wants until player decides to quit
When player quits, the program will display the number of ties, player wins, and computer wins
'''


import random #import random for the computer

def displayMenu(): #function that displays the menu and outlines the instructions and rules
    print("Welcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:")
    print("     Rock smashes scissors")
    print("     Scissors cut paper")
    print("     Paper covers rock")
    print("     If both the choices are the same, it's a tie")
    print("Please choose (0) for rock, (1) for paper or (2) for scissors")

def getComputerChoice(): #function that generates the computer player

    compInput = random.randrange(0, 3) #variable that generates a number between 0 and 2
    if compInput == 0: #if variable is 0, then comp picks rock
        print("The computer chose rock!")
    elif compInput == 1: #if variable is 1, then comp picks paper
        print("The computer chose paper!")
    elif compInput == 2: #if variable is 2, then comp picks scissor
        print("The computer chose scissor!")
    return compInput #return the value to the main function

def getPlayerChoice(): #function that gets user's input

    flag2 = 1 #boolean set to true
    while flag2: #while boolean is true following will happen
        userInput = input("> ") #gets user input
        if userInput == "0" or userInput == "1" or userInput == "2": #if the user chooses any of the 3 numbers then flag2 is false
            flag2 = 0
    if userInput == "0": #user picks rock
        print("You chose rock!")
    elif userInput == "1": #user picks paper
        print("You chose paper!")
    elif userInput == "2": #user picks scissor
        print("You chose scissor!")
    return userInput #returns the user's value to main

def playRound(playerChoice, computerChoice): #function that sets rule for game and compares player and comp values
    if playerChoice == "0" and computerChoice == 0: #if user and comp get same value, then its a tie
        print("You tied with the computer!")
        return 0 #returns a 0 int to main
    elif playerChoice == "1" and computerChoice == 1: #if user and comp get same value, then its a tie
        print("You tied with the computer!")
        return 0 #returns a 0 int to main
    elif playerChoice == "2" and computerChoice == 2:#if user and comp get same value, then its a tie
        print("You tied with the computer!")
        return 0 #returns a 0 int to main
    #Rock Win/Lose
    elif playerChoice == "0" and computerChoice == 2: #user picks rock and comp picks scissors. user wins
        print("Rocks smashes scissors. You win!")
        return 1 #returns one to indicate player win
    elif playerChoice == "0" and computerChoice == 1: #user picks rock and comp picks paper. user loses
        print("Paper covers rock. You lose!")
        return -1 #returns negative one to indicate computer loss
    #Paper Win/Lose
    elif playerChoice == "1" and computerChoice == 0: #user picks paper and comp picks rock. user wins
        print("Paper covers rock. You win!")
        return 1 #returns one to indicate player win
    elif playerChoice == "1" and computerChoice == 2: #user picks scissor and comp picks paper. user loses
        print("Scissor cuts paper. You lose!")
        return -1 #returns negative one to indicate computer loss
    #Scissor Win/Lose
    elif playerChoice == "2" and computerChoice == 0: #user picks rock and comp picks scissor. user loses
        print("Rock smashes scissors. You lose!")
        return -1 #returns one to indicate player loss
    elif playerChoice == "2" and computerChoice == 1: #user picks scissors and comp picks paper. user wins
        print("Scissors cuts paper. You win!")
        return 1 #returns negative one to indicate computer win

def continueGame(): #function that determines whether game will continue
    flag3 = 1 #boolean set to true
    while flag3:  # while boolean is true, following will happen
        userInput2 = input("Do you want to continue playing (y or n)?: ") #asks user if he/she wants to keep playing
        userInput2 = ''.join(userInput2.split()) #removes any spaces
        if userInput2.lower() == "y": #if user inputs "y", then return true and boolean set to false
            return True
            flag3 = 0
        elif userInput2.lower() == "n": #if user inputs "n", then return false and boolean set to false
            return False
            flag3 = 0

def main(): #function where main program occurs

    playerWins = 0 #variable that holds player wins
    computerWins = 0 #varaible that holds computer wins
    ties = 0 #variable that holds ties
    flag1 = True #boolean set true

    while flag1: #while boolean is true
        displayMenu() #calls to display menu
        playerChoice = getPlayerChoice() #calls getplayerchoice function and saves value in playerChoice
        computerChoice = getComputerChoice() #calls getcomputerchoice function and saves value in computerChoice
        score = playRound(playerChoice, computerChoice) #inputs playerChoice and computerChoice and calls playRound function and saves value in score
        if score == 0: #if score is 0, then increase ties by 1
            ties += 1
        elif score == 1: #if score is 1, then increase playerWins by 1
            playerWins += 1
        elif score == -1: #if score is -1, then increase computerWins by 1
            computerWins += 1
        flag1 = continueGame() #returned value of continueGame is saved into flag1
        print("")
        if flag1 == False: #if return value is false, then end game and display the results
            print("Number of ties:",ties)
            print("Number of player win(s):", playerWins)
            print("Number of computer win(s):", computerWins)
            print("")
            print("Thanks for playing!")
        #else, restart the game
main() #intitializes main function
