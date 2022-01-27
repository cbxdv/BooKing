import time
import os
from shutil import get_terminal_size


def clear():
    """
        Clears Screen
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def c_print(s, size=get_terminal_size().columns):
    """
        Centers the text provided
    """
    print(s.center(size))


def loading(count=30, pre=False, post=False):
    """
        Simulates Loading in Console
    """

    if pre:
        clear()
    bar = [
        " [=            ]",
        " [ =           ]",
        " [  =          ]",
        " [   =         ]",
        " [    =        ]",
        " [     =       ]",
        " [      =      ]",
        " [       =     ]",
        " [        =    ]",
        " [         =   ]",
        " [          =  ]",
        " [           = ]",
        " [            =]",
        " [           = ]",
        " [          =  ]",
        " [         =   ]",
        " [        =    ]",
        " [       =     ]",
        " [      =      ]",
        " [     =       ]",
        " [    =        ]",
        " [   =         ]",
        " [  =          ]",
        " [ =           ]",
        " [=            ]",
    ]
    i = 0
    while True:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.05)
        i += 1
        if i == count:
            break
    if post:
        clear()


def seat_row_classifier(seat):

    ch = seat[0]
    n = seat[1:]

    if ch == 'A':
        ch = 0
    elif ch == 'B':
        ch = 1
    if ch == 'C':
        ch = 2
    elif ch == 'D':
        ch = 3
    elif ch == 'E':
        ch = 4
    return int(ch), int(n) - 1


def raw_data_index(a, b):
    n = 0
    if a == 0:
        n = b
    elif a == 1:
        n = 10 + b
    elif a == 2:
        n = 22 + b
    elif a == 3:
        n = 36 + b
    elif a == 4:
        n = 52 + b
    return n


def file_writer(screen_number, time_number, data):
    with open(f'data/S{screen_number}_{time_number}.txt', 'w') as file:
        file.writelines(data)


def array_creator(screen_number, time_number):
    file = open(f'data/S{screen_number}_{time_number}.txt')
    rdata = file.readlines()
    n = 0
    data = []
    for i in rdata:
        t = bool(int(i.strip()))
        data.append(t)
        n += 1
    n = 0
    seat_max = 10
    t_ar = []
    arr = []
    for i in range(5):
        for j in range(seat_max):
            t_ar.append(data[n])
            n += 1
        arr.append(t_ar)
        t_ar = []
        seat_max += 2
    file.close()
    return rdata, arr
