'''
Description:
This program creates a tic tac toe game where a player plays against a computer

'''

import TicTacToeHelper #imported tictactoehelper file
import random #imported RNG

def isValidMove(boardList, spot): #checks for whether the move is valid or not
    if spot != "x" or spot != "o": #if the spot is not an x or o, then it is open and returns true
        return True
    else: #if it is an x or o, then the spot is taken and returns false
        return False

def updateBoard(boardList, spot, playerLetter): #function that updates the player moves
    boardList[spot] = playerLetter #takes the index the player chooses and replaces it with an x or o

def playGame(): #function that plays the game
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"] #board list of a string of 8 numbers
    first = "" #empty string to hold letter of whatever letter decides to go firt
    second = "" #empty string to hold letter of whatever letter decides to go second
    move_counter = 0 #counter that counts the number of moves
    flag7 = 1 #boolean set to true
    while flag7: #while the booalean is true
        userFirst = input("Which player is going first? (x/o): ") #asks what letter is going first
        userFirst = ''.join(userFirst.split())
        if userFirst.lower() == "x": #if x goes first
            first = "x" #sets first variable to x
            second = "o" #sets second variable to o
            flag7 = 0 #boolean set to false
        elif userFirst.lower() == "o": #if o goes first
            first = "o" #sets first variable to o
            second = "x" #sets second variable to x
            flag7 = 0 #boolean set to false
    winCheck = TicTacToeHelper.checkForWinner(boardList, move_counter) #saves parameters into winCheck
    while winCheck == "n": #while there is no winner
        if move_counter == 0: #if the move counter is 0, then print the board
            TicTacToeHelper.printPrettyBoard(boardList)
        if (move_counter % 2) == 0: #if move counter is divisible by 1
            spot = input("Player " + first + " pick a spot: ") #ask the user to pick a spot
            while spot not in boardList: #while the spot is not in the list, then ask the user to pick another spot
                print("Invalid move, please try again")
                spot = input("Player " + first + " pick a spot: ")
            spot = int(spot) #converts str into an int
            playerLetter = first #the player letter becomes the letter of the player who went first
            flag2 = 1 #boolean set to true
            while flag2: #while boolean is true
                validMove = isValidMove(boardList, spot) #checks to see if the move is valid, and saves output in variable
                if validMove is True: #if the output is true
                    updateBoard(boardList, spot, playerLetter) #calls update board function
                    move_counter += 1
                    winCheck = TicTacToeHelper.checkForWinner(boardList, move_counter) #checks for a winner
                    flag2 = 0 #boolean set to false
                else: #output returns false then ask player to pick another spot
                    print("Invalid move, please try again")
                    spot = input("Player " + first + " pick a spot: ")
        else: #if move counter not divisible by 2, then its the computer's turn
            print("Computer is picking a spot...")
            spot = random.randrange(0, 9) #RNG to determine computer's spot
            spot = str(spot) #converts the int into a string
            while spot not in boardList: #while the spot is not in the boardList
                spot = random.randrange(0, 9) #generate another random number
                spot = str(spot) #convert the int into a string
            spot = int(spot) #converts the int back into a int
            playerLetter = second #the player letter becomes the letter of the player who went second
            flag3 = 1 #boolean set to true
            while flag3: #while boolean is true
                validMove = isValidMove(boardList, spot) #calls valid move function and saves the output in a variable
                if validMove is True: #if the output returns true
                    updateBoard(boardList, spot, playerLetter) #call updateBoard function
                    move_counter += 1
                    winCheck = TicTacToeHelper.checkForWinner(boardList, move_counter) #check for a win
                    flag3 = 0 #boolean set to false
                else: #if output returns false
                    spot = random.randrange(0, 9) #regenerate another random number
            print("Computer picked spot", spot)
            TicTacToeHelper.printPrettyBoard(boardList)
        if winCheck == "x": #if winCheck returns x, player x wins and do following
            print("")
            print("Final Board")
            TicTacToeHelper.printPrettyBoard(boardList) #prints the final board
            print("Game Over!")
            print("Player x is the winner!")
            flag4 = 1 #boolean set to true
            while flag4: #while the boolean is true
                userQuit = input("Would you like to play another round? (y/n): ") #ask the user if they want to play another round
                userQuit = ''.join(userQuit.split())
                if userQuit.lower() == "y":  # if user inputs "y", then return true and boolean set to false
                    return True
                    flag4 = 0
                elif userQuit.lower() == "n":  # if user inputs "n", then return false and boolean set to false
                    return False
                    flag4 = 0
        elif winCheck == "o": #if winCheck returns o, player o wins and do following
            print("")
            print("Final Board")
            TicTacToeHelper.printPrettyBoard(boardList) #prints the final board
            print("Game Over!")
            print("Player o is the winner!")
            flag5 = 1 #wihle the boolean is true
            while flag5:
                userQuit2 = input("Would you like to play another round? (y/n): ")
                userQuit2 = ''.join(userQuit2.split())
                if userQuit2.lower() == "y":  # if user inputs "y", then return true and boolean set to false
                    return True
                    flag5 = 0
                elif userQuit2.lower() == "n":  # if user inputs "n", then return false and boolean set to false
                    return False
                    flag5 = 0
        elif winCheck == "s": #if winCheck returns s, then there is a stalemate
            print("")
            print("Final Board:")
            TicTacToeHelper.printPrettyBoard(boardList) #print the final board
            print("Game Over!")
            print("Stalemate reached!")
            flag6 = 1 #boolean set to true
            while flag6: #while the boolean is true
                userQuit3 = input("Would you like to play another round? (y/n): ") #asks the user if they want to play another round
                userQuit3 = ''.join(userQuit3.split())
                print("")
                if userQuit3.lower() == "y":  # if user inputs "y", then return true and boolean set to false
                    return True
                    flag6 = 0
                elif userQuit3.lower() == "n":  # if user inputs "n", then return false and boolean set to false
                    return False
                    flag6 = 0
def main(): #function that rains main program
    flag1 = 1 #boolean set to true
    while flag1: #while boolean is true
        print("Welcome to Tic Tac Toe!")
        flag1 = playGame() #saves output of function into the boolean
        if flag1 == False: #if the boolean is false, then end game
            flag1 = 0
            print("")
            print("Thanks for playing! Goodbye!")
            print("")

main()
