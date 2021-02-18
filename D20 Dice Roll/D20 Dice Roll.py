'''
Description:
This program plays a game where the user wins points by rolling one
of the winning numbers. Before the user’s roll, the program prints out
which numbers qualify for points. The game is played 10 times and
the user’s score is printed at the very end.
'''

def main():

    import random #imported a random # generator

    score = 0 #user's score is defaulted to 0

    for game in range(0, 10): #for loop that runs the game 10 times
        dye = random.randrange(1, 21) #dye RNG that runs through a range of 1 to 20
        case = random.randrange(1, 6) #case RNG that runs through a range of 1 to 6

        print("Now rolling ...") #text
        print("You rolled a", dye) #tells user what number was rolled
        print("You are playing for Case", case) #tells users what cases were assigned
        print("You will win for the following numbers:")

        if case == 1: #below outlines the condition for case1
            win1 = "" #win boolean set to false
            for case1 in range(0, 21, 2): #loop for winning numbers in case 1
                print(case1, end = " ") #prints the winning numbers
                if case1 == dye: #if a number in the case equals the number rolled then boolean is set to true
                    win1 = " "
            print("") #line break
            if win1 == " ": #if boolean is true then score is +50 and informs user
                score += 50
                print("You won 50 points!")
            else: #if the boolean is not true, tell user that he/she did not win
                print("You didn't win :(")
            print("")

        elif case == 2: #below outlines the condition for case2
            win2 = "" #win boolean set to false
            for case2 in range(0, 20, 2): #loop for winning numbers in case 2
                print(case2 + 1, end = " ") #prints the winning numbers
                if (case2 + 1) == dye: #if a number in the case equals the number rolled then boolean is set to true
                    win2 = " "
            print("") #line break
            if win2 == " ": #if boolean is true then score is +50 and informs user
                score += 50
                print("You won 50 points!")
            else: #if the boolean is not true, tell user that he/she did not win
                print("You didn't win :(")
            print("")

        elif case == 3: #below outlines the condition for case3
            win3 = "" #win boolean set to false
            for case3 in range(5, 11, 1): #loop for winning numbers in case 3
                print(case3, end = " ") #prints the winning numbers
                if case3 == dye: #if a number in the case equals the number rolled then boolean is set to true
                    win3 = " "
            print("") #line break
            if win3 == " ": #if boolean is true then score is +50 and informs user
                score += 50
                print("You won 50 points!")
            else: #if the boolean is not true, tell user that he/she did not win
                print("You didn't win :(")
            print("")

        elif case == 4: #below outlines the condition for case 4
            win4 = "" #win boolean set to false
            for case4 in range(10, 22, 2): #loop for winning numbers in case 4
                print(case4, end = " ") #prints the winning numbers
                if case4 == dye:#if a number in the case equals the number rolled then boolean is set to true
                    win4 = " "
            print("") #line break
            if win4 == " ": #if boolean is true then score is +50 and informs user
                score += 50
                print("You won 50 points!")
            else: #if the boolean is not true, tell user that he/she did not win
                print("You didn't win :(")
            print("")

        elif case == 5: #below outlines the condition for case 5
            win5 = "" #win boolean set to false
            for case5 in range(1, 19, 3): #loop for winning numbers in case 5
                print(case5 + 2, end = " ") #prints the winning numbers
                if (case5 + 2) == dye: #if a number in the case equals the number rolled then boolean is set to true
                    win5 = " "
            print("") #line break
            if win5 == " ": #if boolean is true then score is +50 and informs user
                score += 50
                print("You won 50 points!")
            else: #if the boolean is not true, tell user that he/she did not win
                print("You didn't win :(")
            print("")

    print("Your total score is", score) #tells user what their final score is
    print("Thanks for playing!") #tells user thanks for playing



main()
