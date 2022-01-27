from Utils import c_print, clear, loading


def cred_deb(cost):
    while True:
        cno = input("ENTER CREDIT CARD/DEBIT CARD NO. :- ")
        c = len(str(cno))
        if c == 16:
            break
        else:
            c_print("-----INVALID CREDIT/DEBIT CARD NO!-----")

    while True:
        cvv = input("ENTER THE CVV NO. :- ")
        c = len(str(cvv))
        if c == 3:
            break
        else:
            print("INVALID CVV NO")

    while True:
        pin = input("ENTER YOUR PIN :- ")
        p = len(str(pin))
        if p == 4:
            break
        else:
            print("\t\t\tINVALID PIN")

    c_print("-"*30)
    print(f"Amount to be paid: ₹{cost}")
    c = input("DO YOU WANT TO PROCEED (Y/N) : ")
    if c == 'y' or c == 'Y':
        clear()
        loading()
        return True
    else:
        return False


def paytm():
    clear()
    print()
    c_print('*****PAYTM TRANSACTION MODE*****')
    p = 0
    while len(str(p)) != 10:
        p = input('\nENTER YOUR PHONE NO. : ')
        if len(str(p)) == 10:
            break
        else:
            print("The number you have entered is invalid.")
            p = input("\n\t\t\tEnter Your Valid Paytm Number : ".upper())
    c = input("DO YOU WANT TO PROCEED (Y/N) : ")
    if c == 'y' or c == 'Y':
        clear()
        loading()
        return True
    else:
        return False


def pay(cost):
    loading(pre=True)
    print(f"Total Amount: ₹{cost}")
    c_print("+==========================================+")
    c_print("|              PAYMENT OPTIONS             |")
    c_print("|==========================================|")
    c_print("|  1. Credit/Debit Card                    |".upper())
    c_print("|  2. Paytm                                |".upper())
    c_print("|  3. CANCEL PAYMENT AND BACK TO MAIN MENU |")
    c_print("+==========================================+")
    print()
    a = int(input("Enter Your Payment Mode : ".upper()))
    successful = False
    if a == 1:
        successful = cred_deb(cost)
    elif a == 2:
        successful = paytm()
    elif a == 3:
        cho = input('DO YOU WANT TO CANCEL THE TRANSACTION(Y/N) : ')
        if cho == 'y' or cho == 'Y':
            print("The transaction has declined.")
            print("\n\t\t\t Do you like to continue to book a ticket (Y/N)")
            z = input()
            if z == 'y' or z == 'Y':
                pass
        else:
            print("\t\t\t THANK YOU.")
    else:
        print("Invalid Choice.")
    return successful
