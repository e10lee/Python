'''
Description:
This program creates a Harry Potter
vending machine that gives 4 options of drinks to choose from.
User will input amount he would like to pay and which coins he would like to pay with.
The machine will then determine a certain amount with or without a discount.
It will then determine amount of change due back to the user if any.
'''

def main():

    paid = 0 #variable is the amount the user will pay
    price = 0 #empty variable that will represents the total

    #knuts is the currency unit

    print("Please select an item from the vending machine:") #this line asks the user to select an item of thier choice
    print("a) Butterbeer: 58 knuts") #first option is butterbeer for 58 knuts
    print("b) Quill: 10 knuts") #second option is a qull for 10 knuts
    print("c) The Daily Prophet: 7 knuts") #third option is the dialy prophet for 7 knuts
    print("d) Book of Spells: 400 knuts") #fourth option is the book of speels for 400 knuts

    userInput = input("> ") #User will input their option at this line of code
    if userInput.lower() == "a": #Regardless of whether user enters "A" or "a", the program will make the letter a lowercase
        price = 58 #if user enters "a", the program will select butterbeer and set the price = to 58
        option = "Butterbeer"
    elif userInput.lower() == "b": #Regardless of whether user enters "B" or "b", the program will make the letter a lowercase
        price = 10 #program will select quill and set the price to 10
        option = "Quill"
    elif userInput.lower() == "c": #Regardless of whether user enters "C" or "c", the program will make the letter a lowercase
        price = 7 #program will select the daily prophet and set the price to 7
        option = "The Daily Prophet"
    elif userInput.lower() == "d": #Regardless of whether user enters "D" or "d", the program will make the letter a lowercase
        price = 400 #program will select the Book of Spells and set the price to 400
        option = "Book of Spells"
    else: #If the user does not input a, b, c, or d, program will select quill as a default and notify the user
        print("You have entered an invalid option, you will be given a Quill for 10 knuts.")
        price = 10
        option = "Quill"

    print("Please enter amount for each type of coin you would like to use: ") #extracredit: Allow user to input which and how many coins he would like to input
    userKnuts = int(input("Knuts: ")) #converts the string to an int
    paid += userKnuts #Adds amount of knuts that will contribute towards payment
    userSickles = int(input("Sickles: ")) #converts the string to an int
    userSickles = userSickles * 29 #multiplies number of sickles used to pay by the value of the sickle
    paid += userSickles #Adds amount of knuts that will contribute towards payment
    userGalleons = int(input("Galleons: ")) #converst the string to an int
    userGalleons = userGalleons * 493 #multiplies number of galleons used to pay by the value of the galleon
    paid += userGalleons #Adds amount of galleons that will contribute towards payment

    userDiscount = input("Will you share this on instagram? (y/n): ") #asks user if they would like to share their item on instagram
    while userDiscount.lower() != "y" and userDiscount.lower() != "n": #if user does not enter "y" or "n", program will be in a while look until they enter "y" or "n"
        userDiscount = input("Will you share this on instagram? (y/n): ")
    if userDiscount.lower() == "y": #Regardless of whether user enters "Y" or "y", the program will make the letter a lowercase
        print("Thanks! You will get 5 knuts off your purchase.") #user is notified that he/she will receive a discount of "5"
        price -= 5 #subtracts 5 from the total price
        change = paid - price #calculate change by finding difference between amount to be paid by price of item
        print("You bought", option, "for", price, "knuts (with coupon of 5 knuts) and paid with: ") #lets user know what he bought, at what price, and with how many knuts were used to pay
        print(paid, "Knut(s)")

    elif userDiscount.lower() == "n": #Regardless of whether user enters "Y" or "y", the program will make the letter a lowercase
        print("You will not be issued a discount.") #user is notified that he/she will not receive a discount of "5"
        change = paid - price #calculate change by finding difference between amount to be paid by price of item
        print("You bought", option, "for", price, "knuts (with coupon of 0 knuts) and paid with: ") #lets user know what he bought, at what price, and with how many knuts were used to pay
        print(paid, "Knut(s)")

    print("Here is your change (" + str(change) + " knuts):") #prints change due back to user and converts change into a string

    changeinGalleons = change//493 #finds the change in galleons
    change -= changeinGalleons * 493 #subtracts max number of galleons given in change to determine max number of sickles
    changeinSickles = change//29 #finds change in sickles
    change -= changeinSickles * 29 #subtracts max number of sickles given in change to determine max number of knuts
    #left over change is number of knuts to be given back
    print("Knuts:", str(change)) #prints how many knuts are owed back and converts change back to a string
    print("Sickles:", str(changeinSickles)) #prints how many sickles are owed back and converts change back to a string
    print("Galleons:", str(changeinGalleons)) #prints how many galleons are owed back and converts change to a string

main()

