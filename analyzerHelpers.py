# open and print welcome message
def welcomeText():
    welcome_txt = open("Texts/welcome.txt", "r").read()
    print(welcome_txt)


# open and print continuation message
def continuationText():
    welcome_txt = open("Texts/continuation.txt", "r").read()
    print(welcome_txt)


# open and print closing message
def closingText():
    welcome_txt = open("Texts/closing.txt", "r").read()
    print(welcome_txt)


# customer input
def inputBuilder():
    print("Insert Choice below" + "\n"
          + "eg: p, pc, v, vc, q" + "\n")
    customerInput = input("Enter Here: ")
    closingChecker(customerInput)
    inputChecker(customerInput)
    return customerInput


# check customer input
def inputChecker(CustomerChoice):
    while CustomerChoice not in ['p', 'pc', 'v', 'vc', 'q']:
        print("\n" + "Please enter either 'p', 'pc', 'v', 'vc', 'q'")
        CustomerChoice = input("Enter your choice: ")
        closingChecker(CustomerChoice)
        inputChecker(CustomerChoice)
        return CustomerChoice


# closing statement
def closingChecker(CustomerChoice):
    if CustomerChoice == 'q':
        closingText()
        quit()
