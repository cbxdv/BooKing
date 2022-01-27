from Utils import clear, c_print


def movies_print():
    """
    Prints the currently screening movies
    :return: None
    """

    print("Movies currently screening:")
    n = 1
    file = open("data/Movies.txt")
    print("---------------------------------------------------")
    data = file.readlines()
    for i in data:
        print("|", f'{n}'.rjust(5), i.strip().upper().center(40), "|")
        n += 1
    print("---------------------------------------------------")
    file.close()


def upcoming_movies_print():
    """
    Prints the upcoming movies
    :return: None
    """

    # TODO: Update text file with some upcoming movies

    c_print("Upcoming Movies")
    file = open("data/UpcomingMovies.txt")
    c_print("---------------------------------------------------")
    data = file.readlines()
    for i in data:
        c_print("|" + i.strip().upper().center(40) + "|")
    c_print("---------------------------------------------------")
    file.close()


def movie_select():
    clear()
    movies_print()
    ch = int(input("Enter the code of the movie: "))
    with open("data/Movies.txt") as file:
        data = file.readlines()
    name = data[ch - 1].strip()
    return ch, name


def timing_select():
    clear()
    print("Timings available:")
    print('''
        1 : 4:50 pm - 7:20 pm
        2 : 10:30 pm - 1:00 am
    ''')
    timing_slot = input(" Select your preferable time: ")

    if timing_slot == 1:
        time = "4:50 pm - 7:20 pm"
    else:
        time = "10:30 pm - 1:00 am"

    # TODO: Check whether it is full

    return timing_slot, time
