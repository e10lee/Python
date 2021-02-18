'''
Description:
Writes the cars with the max and minimum miles from the epa csv file to another text file
'''


def main():

    years = ["2008", "2009"] #years to choose from
    carTypes = ["SMALL PICKUP TRUCKS 2WD", "SMALL PICKUP TRUCKS 4WD", "STANDARD PICKUP TRUCKS 2WD", "STANDARD PICKUP TRUCKS 4WD", "VANS - CARGO TYPE", "VANS - PASSENGER TYPE", "MINIVAN - 2WD", "MINIVAN - 4WD"] #list of class types we are not looking for
    print("Welcome to the EPA Mileage Calculator")
    userInput = input("What year would you like to view data for? (2008 or 2009): ") #asks user if he/she wants 2008 or 2009
    userInput = ''.join(userInput.split()) #gets rid of whitespace
    while userInput not in years: #while the user does not enter 2008 or 2009 it will keep prompting user to enter a valid year
        print("*Invalid input, please try again!")
        userInput = input("What year would you like to view data for? (2008 or 2009): ")
        userInput = ''.join(userInput.split())
    userFileName = input("Enter the filename to save results to: ") #file for which data will be saved to
    print("Operation Success! Mileage data has been saved to " + userFileName)
    print("Thanks, and have a great day!\n")
    if userInput == "2008": #if user enters 2008
        fileIn = open("epaVehicleData2008.csv", "r") #open 2008 file
        next(fileIn) #skip first line in file
        max = 0
        min = 100
        minList = [""]
        maxList = [""]
        bigList = []
        biggerMaxList = []
        biggerMinList = []
        strMax = ""
        strMin = ""
        for line in fileIn: #for every line in the file
            if line[0] not in carTypes: #if the class is not in carTypes, then do following
                line = line.split(",")
                epaClassMod = line[1:3] #saves the first and second index
                bigList.append(epaClassMod) #appends the variable to another list
                epaMiles = (line[8])
                epaMiles = int(epaMiles)
                epaClassMod.append(epaMiles) #appends the mileage of each car to the list
                if epaMiles > max: #checks and updates max values
                    max = epaMiles
                    del maxList[0]
                    maxList.append(str(max))
                if epaMiles < min: #checks and updates max values
                    min = epaMiles
                    del minList[0]
                    minList.append(str(min))
        for cars in bigList: #for every car in the bigList
            cars[2] = str(cars[2]) #turns the mileage
            if cars[2] == maxList[0]: #if the mileage equals the max, then append the car model and make to the biggermaxlist
                biggerMaxList.append(cars[0:2])
            if cars[2] == minList[0]: #if the mileage equals the min, then append the car model and make to the biggerminlist
                biggerMinList.append(cars[0:2])
        for i in range(len(biggerMaxList)): #for every index in the list
            strMax += "     " #print an indent
            for j in range(len(biggerMaxList[i])): #for every index within the index list
                strMax += biggerMaxList[i][j] + " " #add to strMax the model and the make
            strMax += "\n"
        for i in range(len(biggerMinList)): #for every index in the list
            strMin += "     " #print an indent
            for j in range(len(biggerMinList[i])): #for every index within the index list
                strMin += biggerMinList[i][j] + " " #add to strMax the model and the make
            strMin += "\n"


        fileIn.close() # close the file

    elif userInput == "2009": #if user enters 2009
        fileIn = open("epaVehicleData2009.csv", "r") #open 2009 file
        next(fileIn)
        max = 0
        min = 100
        minList = [""]
        maxList = [""]
        bigList = []
        biggerMaxList = []
        biggerMinList = []
        strMax = ""
        strMin = ""
        for line in fileIn: #for every line in the file
            if line[0] not in carTypes: #if the class is not in carTypes, then do following
                line = line.split(",")
                epaClassMod = line[1:3] #saves the first and second index
                bigList.append(epaClassMod) #appends the variable to another list
                epaMiles = (line[8])
                epaMiles = int(epaMiles)
                epaClassMod.append(epaMiles) #appends the mileage of each car to the list
                if epaMiles > max: #checks and updates max values
                    max = epaMiles
                    del maxList[0]
                    maxList.append(str(max))
                if epaMiles < min: #checks and updates max values
                    min = epaMiles
                    del minList[0]
                    minList.append(str(min))
        fileIn.close()
        for cars in bigList: #for every car in the bigList
            cars[2] = str(cars[2]) #turns the mileage
            if cars[2] == maxList[0]: #if the mileage equals the max, then append the car model and make to the biggermaxlist
                biggerMaxList.append(cars[0:2])
            if cars[2] == minList[0]: #if the mileage equals the min, then append the car model and make to the biggerminlist
                biggerMinList.append(cars[0:2])

        for i in range(len(biggerMaxList)): #for every index in the list
            strMax += "     "
            for j in range(len(biggerMaxList[i])): #for every index within the index list
                strMax += biggerMaxList[i][j] + " " #add to strMax the model and the make
            strMax += "\n"

        for i in range(len(biggerMinList)):
            strMin += "     "
            for j in range(len(biggerMinList[i])):
                strMin += biggerMinList[i][j] + " "
            strMin += "\n"



    fileOut = open(userFileName, "w") #prints everything to the user's selected file
    print("EPA City MPG Calculator " + "(" + userInput + ")", file=fileOut)
    print("---------------------",  file=fileOut)
    print("Maximum Mileage (city):", max, file=fileOut)
    print(strMax, file=fileOut)
    print("Minimum Mileage (city):", min, file=fileOut)
    print(strMin, file=fileOut)
    fileOut.flush()
    fileOut.close()

main()
