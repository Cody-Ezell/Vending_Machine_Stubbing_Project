#########################################################################################################
# Programmer: Cody Ezell
# Date Created: 9/15/20
# File Name: Vending_Machine_Stubbing_Project.py
# Description: This program implements a vending machine. The user
#              shall make a selection from the menu, then the program
#              shall output that the machine will now vend that selection.
#              This program is stubbed for basic formatting purposes.
# Function List:
#   displayMenu - displays the menu for the vending machine
#   calculateAndDispenseBeverage - Filters the user's inputted choice,
#                                  then calls the calculate function and dispense function.
#   main - main function of the program
# Global Variables
#   CANCELLED - used to indicate if user has pressed the cancel button to cancel transaction and exit
#########################################################################################################


# Global variables
CANCELLED = False    # used to indicate if user has pressed the cancel button to cancel transaction and exit


#####################################################################
# Function: displayMenu - displays the menu for the vending machine
#####################################################################
def displayMenu():
    print("""
    All beverages $1.00
    -------------------
    1. Coke 
    2. Sprite
    3. Root Beer
    4. Dr. Pepper
    5. Peach Sunkist
    6. Ginger Ale
    7. Mountain Dew
    8. Creme Soda
    9. Sparkling Water
    10. Water
    E. - CANCEL & EXIT
    """)

###################################################################################
# Function: calculateAndDispenseBeverage - Filters the user's inputted choice,
# then calls the calculate function and dispense function.
###################################################################################
def calculateAndDispenseBeverage(selection):
    if selection == '1':
        print("Item 1 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '2':
        print("Item 2 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '3':
        print("Item 3 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '4':
        print("Item 4 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '5':
        print("Item 5 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '6':
        print("Item 6 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '7':
        print("Item 7 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '8':
        print("Item 8 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '9':
        print("Item 9 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == '10':
        print("Item 10 incomplete")
        print("Begin calculating price. Pricing function not implemented")
        print("Begin dispensing drink. Dispense function not implemented")
    elif selection == 'e' or selection == 'E':
        print("CANCELING TRANSACTION AND EXITING")
        global CANCELLED   # Global keyword allows you to modify the variable outside of the current scope.
        CANCELLED = True
    else:
        print("INCORRECT OR UNDEFINED SELECTION - TRY AGAIN")


#####################################################################
# Function: main - main function of the program
#####################################################################
def main():
    # Displays the name of the vending machine
    print("\nBestest Most Wonderfulest Vending Machine")
    print("-----------------------------------------")

    # while loop that repeats the menu and ability for user to select a choice until cancelled by user.
    while not CANCELLED:
        displayMenu()
        selection = input("Make a selection (1-10): ")
        calculateAndDispenseBeverage(selection)


if __name__ == "__main__":
    main()