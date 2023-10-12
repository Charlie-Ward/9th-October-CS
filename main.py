loop = True
while loop:
    validUser = False

    ticketValid = input("Do you have a ticket Yes/No: ")
    if ticketValid == "Yes":
        validUser = True
    elif ticketValid == "Admin":
        loop = False
    else:
        age = int(input("What is your age: "))
        if age < 15:
            print("This museum is for 15+ years only")
        else:
            purchase = input("Do you have £3 for a ticket Yes/No: ")
            if purchase == "Yes":
                validUser = True
            else:
                print("Ticket purchase cancelled")
    if validUser == True:
        print("Please enter now")
