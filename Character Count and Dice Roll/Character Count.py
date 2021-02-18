'''
Description:
This program asks for the user to input a sentence, which
the program will then print out each letter of the alphabet followed by
the number of asterisks representing how many times that letter/special character appears
in the sentence.
'''
def main():

    userMsg = input("Please enter a sentence:") #tells user to enter a sentence
    print("Here is the character distribution:")
    alphabet = "abcdefghijklmnopqwrstuvwxyz" #string with the full alphabet. Will be checking against in for loops

    specialCount = 0 #special character count is set to 0

    for char in userMsg: #for loop for special character in user's message
        if char.isalpha() is False and char.isspace() is False: #for each character in the message, if its not an alphabet or a space...
            specialCount += 1 #then the special char count increases by 1

    print("special characters: ", end="") #print text for special charactesr

    if specialCount == 0: #if the special char count is 0, then print "NONE"
        print("NONE")
    else: #if not 0, then run code below
        while specialCount > 0: #if special count is greater than 0, then print an * and subtract 1 from the special count
            print("*", end="")
            specialCount -= 1
        print("")

    for check in alphabet: #for loop for the alphabets
        count = 0 #count is set to 0
        print(check + ": ", end="") #prints each alphabet
        for letter in userMsg: #for loop for alphabet in user's message
            if check.upper() == letter or check.lower() == letter: #if a letter in the alphabet matches a letter in the msg,
               count += 1 #then increase the count by 1
        if count == 0: #if count is equal to 0, then print NONE
            print("NONE")
        else: #if not, then print an asterick for every time the letter appears
            tempCount = 0
            while (tempCount < count): #while the count is greater than tempCount, then increase the tempCount by 1
                print("*", end = "")
                tempCount += 1
            print("")

main()
