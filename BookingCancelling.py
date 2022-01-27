import Utils
import MoviesTimings
import Seating
import Payment


def _city():
    """
    Selecting city from the specified cities
    """

    Utils.clear()
    print()
    print("Hello. Welcome to the world of movie ticket bookings ")

    print(
        "As per the protocols followed in this covid situation as released by the central government,"
        " the theatres in the hotspots will not function until or unless lockdown is relaxed")

    print("In which city do you want to watch the movie: ")
    print("1. Coimbatore")
    print("2. Mumbai")
    print("3. Cochin")
    print("4. Bangalore")
    print("5. Delhi")

    ch = int(input('\nChoose your favorable city: '))

    if ch == 1:
        print("The city entered is Coimbatore.")
        return
    elif ch == 2 or ch == 3 or ch == 4 or ch == 5:
        print("This city theatre is unavailable due to covid-19 lockdown.")
        print("Sorry for the inconvenience caused")
    else:
        print("Invalid choice. Please Enter a the city in the given options.")
    input("Enter to continue.....")
    _city()


def _center():
    """
    Selecting theater from the specified theaters
    """

    Utils.clear()
    print()
    print("Select theatre of your choice: ")
    print("1. Spi Cinemas")
    print("2. Fun Cinemas")
    print("3. INox")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print("The movie theatre is Spi Cinemas.")
        return
    elif ch == 2 or ch == 3:
        print("This theatre is unavailable due to covid-19 lockdown.")
        print("Sorry for the inconvenience caused")
    else:
        print("Invalid choice. Please enter from the given options.")
    input("Enter to continue.....")
    _center()


def book_tickets():
    """
    Book tickets for a show
    :return: None
    """

    _city()
    _center()
    movie_number, movie_name = MoviesTimings.movie_select()
    time_number, time = MoviesTimings.timing_select()
    raw_data, array = Utils.array_creator(movie_number, time_number)
    seats = Seating.seat_select(array)
    if len(seats) == 0:
        return
    converted_seats = []
    for seat in seats:
        a, b = Utils.seat_row_classifier(seat)
        converted_seats.append((a, b))
        if not Seating.seat_availability(array, a, b):
            print("All the seats you have chosen is not available. Try again")
            input("Enter to go home...")
            return
    payment = Payment.pay(len(seats) * 150)
    if payment:
        print("Payment successful")
    else:
        print("Payment not successful")
        return
    for s in converted_seats:
        a = s[0]
        b = s[1]
        array[a][b] = True
        ind = Utils.raw_data_index(a, b)
        raw_data[ind] = "1\n"
    Utils.file_writer(movie_number, time_number, raw_data)
    Utils.clear()
    display_ticket(movie_name, time, seats, )
    input("Enter to go home.....")


def cancel_tickets():
    """
     Cancel tickets for a show
     :return: None
     """

    _city()
    _center()
    movie_number, movie_name = MoviesTimings.movie_select()
    time_number, time = MoviesTimings.timing_select()
    raw_data, array = Utils.array_creator(movie_number, time_number)
    seats = Seating.seat_select(array)
    if len(seats) == 0:
        return
    converted_seats = []
    for seat in seats:
        a, b = Utils.seat_row_classifier(seat)
        converted_seats.append((a, b))
        if Seating.seat_availability(array, a, b):
            print("Invalid Seat Selection.")
            input("Enter to go home...")
            return
    c = input("DO YOU WANT TO PROCEED (Y/N): ")
    if c == 'n' or c == 'N':
        return
    Utils.loading()
    for s in converted_seats:
        a = s[0]
        b = s[1]
        array[a][b] = False
        ind = Utils.raw_data_index(a, b)
        raw_data[ind] = "0\n"
    Utils.file_writer(movie_number, time_number, raw_data)
    Utils.clear()
    print("Your tickets are canceled. Amount will be refund soon to your bank account.")
    input("Enter to go home.....")


def display_ticket(movie_name, time, seats):
    print()
    Utils.c_print("-------------------------------------")
    Utils.c_print('Spi Cinemas, Coimbatore')
    Utils.c_print(f'Movie Name: {movie_name}')
    Utils.c_print(f'Time: {time}')
    Utils.c_print(f'Seat(s): {seats}')
    Utils.c_print(f'Price: {len(seats) * 150}')
    Utils.c_print("-------------------------------------")
    print("Take a screenshot of this to admit in the theater.")
    print()
