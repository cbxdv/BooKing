import shutil

from Utils import c_print, loading, clear
from MoviesTimings import movies_print, upcoming_movies_print
from BookingCancelling import book_tickets, cancel_tickets


def home():
    clear()
    size = shutil.get_terminal_size().columns
    print()
    print("#        #        #".center(size))
    print("##      ###      ##".center(size))
    print("###    #####    ###".center(size))
    print("####  #######  ####".center(size))
    print("###################".center(size))
    print("###################".center(size))
    print("###################".center(size))
    print("*******************".center(size))
    print()
    print(" #######,     #####       #####           ##   ##         ##    ##    #      ########  ".center(size))
    print(" ##    ##    ##   ##     ##   ##          ##  ##          ##    # #   #     ##         ".center(size))
    print(" #######    ##     ##   ##     ##  #####  #####    #####  ##    #  #  #   ##   ######  ".center(size))
    print(" ##    ##    ##   ##     ##   ##          ##  ##          ##    #   # #    ##   ##  ## ".center(size))
    print(" #######      #####       #####           ##   ##         ##    #    ##     ######  ## ".center(size))

    print("\n\n")
    c_print("---------------------------------------------------")
    c_print("1. Home")
    c_print("2. Current Movies")
    c_print("3. Upcoming Movies")
    c_print("4. Book Tickets")
    c_print("5. Cancel Tickets")
    c_print("6. Exit")
    c_print("---------------------------------------------------")
    print()

    ch = int(input("Enter choice: ".rjust(30)))
    return ch


def main():
    try:
        loading(pre=True)
        ch = home()
        if ch == 1:
            main()
        elif ch == 2:
            clear()
            movies_print()
            input("Enter to continue.....")
            main()
        elif ch == 3:
            clear()
            upcoming_movies_print()
            input("Enter to continue.....")
            main()
        elif ch == 4:
            book_tickets()
            main()
        elif ch == 5:
            cancel_tickets()
            main()
        elif ch == 6:
            c_print("Thank You!")
            return
    except:
        clear()
        print("Something happened!")
        input("Enter to continue.....")
        main()


if __name__ == '__main__':
    main()
