# ATM machine Coad.
print("Welcome to ABC Bank")
restart = ("Y")
chances = 4
balance = 10000
while chances >=0:
    pin = int(input("Please Enter your 4 digit pin coad : "))
    if pin==(1234):
        print("You Enter your Pin Correctly \n")
        while restart not in ('n','NO','no','n'):
            print("Please Press 1 for your balance \n")
            print("Please Press 2 for your withdraw \n")
            print("Please Press 3 for your Pay_in \n")
            print("Please Press 4 for your Return Card \n")
            option = int(input("What would you like to choose ? :  "))
            if option == 1:
                print("Your Balance is $",balance )
                break
            if option == 2:
                option2 =("Y")
                withdraw = float(input("How Much would you like to withdraw ?\n$100/$200/$300/$500 For other enter 5 : "))
            elif withdraw in [100,200,300,500]:
                balance = balance - withdraw
                print("\n Your balance is now $",balance)
                restart = input("What would you like to do? ")
            elif restart in ('n','NO','no','n'):
                print("Thank you for banking with ABC Bank")
                break
            elif withdraw !=[100,200,300,500]:
                print("Invalid amount, Please Re-try\n")
                restart=("Y")
            elif withdraw == 5:
                withdraw = float(input("Please Enter the desired amount : "))
            elif option == 3:
                 pay_in = float(input("How much would you like to payin"))
                 balance = balance + pay_in
                 print("\n Your Balance is now $",balance)
                 restart = input("What would you like to do?")
            if restart in ('n','NO','no','n'):
                print("Thank you for Banking with ABC Bank")
            elif option == 4:
                print("Please Wait while your card is returned.......\n")
                print("Thank you for banking with ABC Banking")
                break
            else:
                print("Please Enter a Correct number \n")
                restart = ("Y")
    elif pin != ("1234"):
        print("Incorrect Pin Try again")
        chances = chances - 1
    if chances == 0:
        print("\n No more try, Contact support@absbank.co.in")
        break