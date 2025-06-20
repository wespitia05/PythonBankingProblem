# python banking problem

# divide into separate sections:
# show balance, withdrawal, deposit

# this function will show us the balance
def show_balance ():
    pass

# this function will handle the deposit methods
def deposit ():
    pass

# this function will handle the withdrawal methods
def withdrawal ():
    pass

# initialize our varaibles
balance = 0
is_running = True # if false, exit program

# while the function running is true, otherwise exit
while is_running:
    # prints out basic menu
    print ("Banking Program")
    print ("1. Show Balance")
    print ("2. Deposit")
    print ("3. Withdrawal")
    print ("4. Exit")

    # allow user to enter a choice from the menu
    choice = input ("Enter your choice (1-4): ")

    # if user chooses 1, call show_balance funciton
    if choice == "1":
        show_balance ()
    # if user chooses 2, call deposit function
    elif choice == "2":
        deposit ()
    # if user chooses 3, call withdrawal function
    elif choice == "3":
        withdrawal ()
    # if user chooses 4, set is_running to false and exit system
    elif choice == "4":
        is_running = False