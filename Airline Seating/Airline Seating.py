'''
Description:
This program assigns up to 10 seats on a flight.
It gives the user the options to assign seats, print and update seat maps
and print boarding passes for which he can search via seat number or name.
'''

def main():

    totalSeats = 10
    numfilledSeats = 0
    seatList = ([""] * 10)
    flag1 = 1

    while flag1 == 1:
        print("1: Assign Seat")
        print("2: Print Seat Map")
        print("3: Print Boarding Pass")
        print("-1: Quit")
        userInput = input(">: ")
        userInput = ''.join(userInput.split())
        if userInput == "1":
            if numfilledSeats < totalSeats:
                userName = input("Please enter your first name: ")
                userName = ''.join(userName.split())
                seatList[numfilledSeats] = userName
                numfilledSeats += 1
            else:
                print("Next flight leaves in 3 hours")
        elif userInput == "2":
            print("**********************************")
            for seat in range(1, 11):
                names = seatList[seat - 1]
                if names == "":
                    names = "EMPTY"
                print("Seat #" + str(seat) + ":" , names )
            print("**********************************")
        elif userInput == "3":
            flag3 = 1
            while flag3 == 1:
                print("Type 1 to get Boarding Pass by seat number")
                print("Type 2 to get Boarding Pass by name")
                userInput2 = input(">: ")
                userInput2 = ''.join(userInput2.split())
                if userInput2 == "1" or userInput2 == "2":
                    flag3 = 0
            if userInput2 == "1":
                byNum = int(input("What is the seat number?"))
                if byNum <= 10:
                    seatNum = seatList[byNum - 1]
                    if seatNum != "":
                        print("========BOARDING PASS=======")
                        print("Seat #: " + str(byNum))
                        print("Passenger Name: " + seatNum)
                        print("============================")
                    else:
                        print("Invalid number --- no boarding pass found")
                else:
                    print("Invalid number --- no boarding pass found")
            elif userInput2 == "2":
                byName = input("What is the passenger name: ")
                byName = ''.join(byName.split())
                flag5 = 1
                for seat in range(1, 11):
                    name = seatList[seat - 1]
                    if byName.lower() == name.lower():
                        flag5 == 0
                if flag5 == 0:
                    print("Name does not exist")
                else:
                    seatAppoint = (seatList.index(byName) + 1)
                    print("========BOARDING PASS=======")
                    print("Seat #: " + str(seatAppoint))
                    print("Passenger Name: " + byName)
                    print("============================")
        elif userInput == "-1":
            flag1 = 0
main()
