'''
Description:
Caesar cipher program that encrypts a message and then decrypts it
'''
def main():

    flag1 = 1 #boolean
    alphabet = "abcdefghijklmnopqrstuvwxyz" #string for the plain text
    encrypt = [] #list variable for encrypted text
    decrypt = [] #list variable for decrypted text
    while flag1: #while boolean is true
        userInput = input("Enter a message: ")
        if all(char.isalpha() or char.isspace() for char in userInput):
            flag1 = 0

    userShift = input("Enter a number to shift by (0 to 25): ") #asks user to input a number
    while userShift.isdigit() == False: #if input is not number ask again
        userShift = input("Enter a number to shift by (0 to 25): ")
    shiftNum = int(userShift) #converts the number into an int
    newAlphabet = alphabet[shiftNum:] + alphabet[:shiftNum] #cipher alphabet is created by shifting over the alphabet by the number the user inputted and placing those letters at the end


    for letter1 in userInput: #for each letter in the userInput
        if letter1 != " " and letter1.isalpha() == True: #if the letter does not equal a space
            encrypt += newAlphabet[alphabet.index(letter1)] #find the index of that letter in the alphabet string and correspond it to that of the cipher and add that letter to the encrypted list
        else:
            encrypt += letter1 #if the letter equals a space, then add that to the list

    print("Encrypting message ... ")
    encryptString = "".join(encrypt) #converts the list to a string
    print("     Encrypyed message:", encryptString) #prints the string

    for letter2 in encryptString: #for each letter in the string
        if letter2 != " ": #if it does not equal a space
            decrypt += alphabet[newAlphabet.index(letter2)] #find the index of the cipheralphabet and correspond it to that of the alphabet and add it to the decryption list
        else:
            decrypt += " " #if its a space add it to the list

    print("Decrypting message ... ")
    decryptString = "".join(decrypt) #convert list into a string
    print("     Decrypted message:", decryptString) #print out decryption string
    print("     Original message:", userInput) #print out original message
main()

