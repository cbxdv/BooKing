import shutil
import colorama
from colorama import Fore, Back

from Utils import clear

colorama.init(autoreset=True)


def _screen():
    size = shutil.get_terminal_size().columns
    print(Fore.LIGHTBLUE_EX + "   /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\  ".center(size))
    print(Fore.LIGHTBLUE_EX + "  %                                                                          %  ".center(size))
    print(Fore.LIGHTBLUE_EX + " %                           SCREEN THIS WAY                                  % ".center(size))
    print(Fore.LIGHTBLUE_EX + "%                                                                              %".center(size))
    print(Fore.LIGHTBLUE_EX + "````````````````````````````````````````````````````````````````````````````````".center(size))


def _seat_index():
    print(Back.RED + '  ', end='')
    print(" - Not Available")
    print(Back.LIGHTGREEN_EX + '  ', end='')
    print(" - Available")


""" 
                        ##  ##  ##  ##  ##  ##  ##  ##  ##  ##                     10 - 1 to 10
                      ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##                   12 - 11 to 22 
                ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##             14 - 23 to 36
              ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##           16 - 37 to 52
        ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##     18 - 53 to 70
"""


def _seating(arr):
    clear()
    size = shutil.get_terminal_size().columns
    _seat_index()
    _screen()
    n = 0
    char_count = 38
    seat_row = 65
    for i in arr:
        line = " " * ((size - char_count - 8) // 2)
        char_count += 8
        for j in i:
            if j:
                line += Fore.RED + f"{chr(seat_row)}{n+1}"
            else:
                line += Fore.LIGHTGREEN_EX + f"{chr(seat_row)}{n + 1}"
            n += 1
            line += Back.RESET + "  "
        print(line)
        seat_row += 1
        n = 0


def seat_select(arr):
    _seating(arr)
    seats = []
    s = input("Enter seats (separated by spaces): ")
    seats = s.split()
    return seats


def seat_availability(array, a, b):
    return not array[a][b]
