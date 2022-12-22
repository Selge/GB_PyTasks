import sys


def start_menu():
    print("""Welcome to GB Python homework #1.
    Please, choose a task from the list below or push 'q' to exit the program:
    - 1. Task 1
    - 2. Task 2
    - 3. Task 3
    - 4. Task 4
    - 5. Task 5
    """)
    match_pointer()


def match_pointer():
    task_pointer = symbol_request("Please, make your choice:  ", str).lower()
    match task_pointer:
        case '1':
            task_1()
        case '2':
            task_2()
        case '3':
            task_3()
        case '4':
            task_4()
        case '5':
            task_5()
        case 'q':
            sys.exit()
        case _:
            print("Please, use built-in options!")
            match_pointer()


def task_1():
    """ Задание 1. """

    # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
    # является ли этот день выходным.
    # Пример:
    # - 6 -> да
    # - 7 -> да
    # - 1 -> нет

    print("GB Python homework. Stage 1. Task 1.")
    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

    day = symbol_request("Please, type in target weekday number:  ", int)

    if 5 >= day >= 1:
        print(f"No, {weekdays[day - 1]} (day {day}) is not a weekend. It's a business day, get back to work!")
    elif 7 >= day >= 6:
        print(f"Yes, {weekdays[day - 1]} (day {day}) is a weekend. Have some rest!")
    else:
        print("Wrong day number! Use numbers in range 1 - 7!")
        task_1()

    anything_else(task_1)


def task_2():

    """ Задание 2. """

    #  Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    #  для всех значений предикат.

    print("GB Python homework. Stage 1. Task 2.")
    x = bool(symbol_request("Please, set up 'X' value:  ", bool))
    y = bool(symbol_request("Please, set up 'Y' value:  ", bool))
    z = bool(symbol_request("Please, set up 'Z' value:  ", bool))

    if (not (x or y or z)) == (not x and not y and not z):
        print("The statement is true.")
    else:
        print("The statement is false.")

    anything_else(task_2)


def task_3():
    """ Задание 3. """

    # Напишите программу, которая принимает на вход координаты точки (X и Y),
    # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    # в которой находится эта точка (или на какой оси она находится).
    # Пример:
    # - x=34; y=-30 -> 4
    # - x=2; y=4-> 1
    # - x=-34; y=-30 -> 3

    print("GB Python homework. Stage 1. Task 3.")
    point_x = int(symbol_request("Please, set up 'x' coordinates:  ", int))
    point_y = int(symbol_request("Please, set up 'y' coordinates:  ", int))

    if float('inf') > point_x > 0 and float('inf') > point_y > 0:
        print(f"The coordinates {point_x}.{point_y} belong to the first quarter.")
    elif float('-inf') < point_x < 0 < point_y < float('inf'):
        print(f"The coordinates {point_x}.{point_y} belong to the second quarter.")
    elif float('-inf') < point_x < 0 and float('-inf') < point_y < 0:
        print(f"The coordinates {point_x}.{point_y} belong to the third quarter.")
    elif float('inf') > point_x > 0 > point_y > float('-inf'):
        print(f"The coordinates {point_x}.{point_y} belong to the fourth quarter.")

    anything_else(task_3)


def task_4():
    """ Задание 4. """

    # Напишите программу, которая по заданному номеру четверти,
    # показывает диапазон возможных координат точек в этой четверти (x и y).

    print("GB Python homework. Stage 1. Task 4.")

    quarters = {
        1: "Available coordinates: x: 0 to infinity; y: 0 to infinity.",
        2: "Available coordinates: x: negative infinity to 0; y: 0 to infinity.",
        3: "Available coordinates: x: negative infinity to 0; y: negative infinity to 0.",
        4: "Available coordinates: x: 0 to infinity; y: negative infinity to 0."
    }

    quarter_num = int(symbol_request("Please, enter the quarter number:  ", int))

    if 4 >= quarter_num >= 1:
        print(quarters[quarter_num])
    else:
        print("Wrong quarter number! Use digits from 1 to 4.")
        task_4()

    anything_else(task_4)


def task_5():
    """ Задание 5. """

    # Напишите программу, которая принимает на вход координаты двух точек
    # и находит расстояние между ними в 2D пространстве.
    # Пример:
    # - A (3,6); B (2,1) -> 5,09
    # - A (7,-5); B (1,-1) -> 7,21

    print("GB Python homework. Stage 1. Task 5.")

    point_a_x = int(symbol_request("Please, set up 'x' coordinates of the point 'A':  ", int))
    point_a_y = int(symbol_request("Please, set up 'y' coordinates of the point 'A':  ", int))
    point_b_x = int(symbol_request("Please, set up 'x' coordinates of the point 'B':  ", int))
    point_b_y = int(symbol_request("Please, set up 'y' coordinates of the point 'B':  ", int))

    coordinates = (((point_b_x - point_a_x) ** 2 + (point_b_y - point_a_y) ** 2) ** 0.5)
    print(f"The distance between point A {point_a_x, point_a_y} and point B {point_b_x, point_b_y} is: {coordinates:5.2f}")

    anything_else(task_5)


def symbol_request(request, datatype):
    request = request
    datatype = datatype
    try:
        symbol = datatype(input(request))
    except ValueError:
        print("Invalid data type!")
        symbol_request(request, datatype)

    return symbol


def anything_else(task):
    print("""
    Do you want anything else?
    Please, type:
    'a' - to start the current task again
    'm' - to get back to the main menu
    'q' - to exit the program
    """)
    again = symbol_request("Please, make your choice:  ", str).lower()
    match again:
        case 'a':
            task()
        case 'm':
            start_menu()
        case 'q':
            sys.exit()
        case _:
            print("Please, use built-in options!")
            anything_else(task)


if __name__ == '__main__':
    start_menu()
