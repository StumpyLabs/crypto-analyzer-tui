import coingecko
import time


def run():
    # welcome text
    welcomeText()
    time.sleep(10)

    # welcome choices
    welcomeChoicesText()
    time.sleep(8)

    # repeat builder until quit
    inputBuilder()


# customer input
def inputBuilder():
    print("Insert Choice below" + "\n"
          + "eg: mc, p, pc, v, al, ah, q" + "\n")
    customerInput = input("Enter Here: ")
    closingChecker(customerInput)
    inputChecker(customerInput)

    # continuation until quit
    while customerInput != "q":
        # continuation text
        continuationText()

        # customer input
        inputBuilder()


# check customer input
def inputChecker(CustomerChoice):
    while CustomerChoice not in ['mc', 'p', 'pc', 'v', 'al', 'ah', 'q']:
        print("\n" + "Please enter either 'mc', 'p', 'pc', 'v', 'al', 'ah', 'q'")
        CustomerChoice = input("Enter your choice: ")
        closingChecker(CustomerChoice)
    coingecko.runCoingecko(CustomerChoice)


# closing statement
def closingChecker(CustomerChoice):
    if CustomerChoice == 'q':
        closingText()
        quit()


def welcomeText():
    welcome_txt = open("Texts/welcome.txt", "r").read()
    print(welcome_txt)


def welcomeChoicesText():
    welcome_txt = open("Texts/welcomeChoices.txt", "r").read()
    print(welcome_txt)


# open and print continuation message
def continuationText():
    welcome_txt = open("Texts/continuation.txt", "r").read()
    print("\n" + welcome_txt)


# open and print closing message
def closingText():
    welcome_txt = open("Texts/closing.txt", "r").read()
    print(welcome_txt)
