'''
Description: User enters a set of numbers and the program
will state the maximum, minimum, and average
'''


def main():

    flag1 = 0 #flag1 is set to 0

    while flag1 == 0: #while flag1 is set to 0, the following code will run including the while loops below

        flag2 = 0 #flag2 is set to 0

        while flag2 == 0: #while flag 2 is set to 0, the following code will run
            count = 0 #variable to count number of times a number is inputted by user
            sum = 0 #variable that will calculate sum of the numbers

            print("Input an integer greater than or equal to 0 (-1 to quit)") #asks user to input an integer and outlines instructions
            userInput = int(input(">")) #where the user inputs the numbers
            max = userInput #sets the input number as the max
            min = userInput #sets the input number as the min
            while userInput >= 0: #while the user input is greater than or equal to 0, following code will run
                sum += userInput #the number inputted will be addded to calculate the sum of all the numbers
                count += 1 #every time a user inputs a number the count increases by 1
                userInput = int(input(">")) #program will ask user to input number again
                if userInput != -1: #As long as the user does not enter -1, the following code will run
                    if userInput >= max: #checks to see if the new inputted number is greater than the current max
                        max = userInput #if inputted number is greater than the current max, that number then becomes the new max
                    if userInput <= min: #checks to see if the new inputted number is less than the current min
                        min = userInput #if inputted number is less than the current min, that number then becomes the new min

            if userInput == -1: #if user inputs -1, following code will run
                print("The largest number is", max) #prints the max
                print("The smallest number is", min) #prints the min
                average = sum / count #calculates the average by dividing sum by the count
                print("The average number is", average) #prints the calculated average of the numbers
                sum = 0 #sets the sum back to 0
                count = 0 #sets the count back to 0
                flag2 = 1 #sets flag 2 back to 1, to prevent program from running again

            userStartover = input("Would you like to enter another set of numbers? (y/n):") #asks the user if he/she would like to do program again
            while userStartover.lower() != "n" and userStartover.lower() != "y": #while the input is not y or n, it will keep asking user the question
                userStartover = input("Would you like to enter another set of numbers? (y/n):")
            if userStartover.lower() == "n": #if user puts no, then program will end and whole program will stop running
                print("Goodbye!")
                flag1 = 1
            elif userStartover.lower() == "y": #if the user says yes, then the program will reinitialize itself b/c while flag1 = 0, then program will keep running
                flag1 = 0


main()
