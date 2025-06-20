# python banking problem

# divide into separate sections:
# show balance, withdrawal, deposit

# this function will show us the balance
def show_balance(balance):
    # :.2f displays 2 decimal places
    print ("*********************")
    print (f"Your balance is ${balance:.2f}")

# this function will handle the deposit methods
def deposit():
    # amount will be a float type (integer w/ decimal)
    # will prompt user to enter amount to deposit
    print ("*********************")
    amount = float(input("Enter and amount to be deposited: "))

    # if they entered an amount les than 0, aka negative
    # print error msg
    if amount < 0:
        print ("*********************")
        print ("That is not a valid amount")
        return 0
    # else return the amount deposited
    else:
        print ("*********************")
        print (f"Amount deposited: ${amount:.2f}")
        return amount

# this function will handle the withdrawal methods
def withdrawal(balance):
    # amount will be a float type (integer w/ decimal)
    # will prompt user to enter amount to withdraw
    print ("*********************")
    amount = float(input("Enter amount to be withdrawn: "))

    # if amount is greater than balance, print error msg
    if amount > balance:
        print ("*********************")
        print ("Insufficient funds")
        return 0
    # if amount is less than 0, print error msg
    elif amount < 0:
        print ("*********************")
        print ("Amount must be greater than 0")
        return 0
    # otherwise return valid amount to be withdrawn
    else: 
        print ("*********************")
        print (f"Amount withdrawn: ${amount:.2f}")
        return amount

def main():
    # initialize our varaibles
    balance = 0
    is_running = True # if false, exit program

    # while the function running is true, otherwise exit
    while is_running:
        # prints out basic menu
        print ("*********************")
        print ("   Banking Program   ")
        print ("*********************")
        print ("1. Show Balance")
        print ("2. Deposit")
        print ("3. Withdrawal")
        print ("4. Exit")
        print ("*********************")

        # allow user to enter a choice from the menu
        choice = input ("Enter your choice (1-4): ")

        # if user chooses 1, call show_balance funciton
        if choice == "1":
            show_balance(balance)
        # if user chooses 2, call deposit function
        elif choice == "2":
            # deposit will be added on top of the balance
            balance += deposit()
        # if user chooses 3, call withdrawal function
        elif choice == "3":
            balance -= withdrawal(balance)
        # if user chooses 4, set is_running to false and exit system
        elif choice == "4":
            is_running = False
            print ("*********************")
            print ("Thank you have a nice day!")
            print ("*********************")
        # if user enters invalid choice, print error msg
        else:
            print ("*********************")
            print ("That is not a valid choice")

if __name__ == '__main__':
    main()