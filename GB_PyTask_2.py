import sys


def start_menu():
    print("""Welcome to GB Python homework #2.
    Please, choose a task from the list below or push 'q' to exit the program:
    - 1. Task 1
    - 2. Task 2
    - 3. Task 3
    - 4. Task 4
    - 5. Task 5
    """)
    match_pointer()

def match_pointer():
    task_pointer = str(symbol_request("Please, make your choice:  ")).lower()
    match task_pointer:
        case '1':
            task_1()
        case '2':
            task_2()
        case '3':
            task_3()
        case '4':
            task_4()
        case 'q':
            sys.exit()
        case _:
            print("Please, use built-in options!")
            match_pointer()


def task_1():
    """ Задание 1. """

    #  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    #  Пример:
    # - 6782 -> 23
    # - 0,56 -> 11

    print("GB Python homework. Stage 2. Task 1.")

    try:
        number = float(symbol_request("Please, type in target weekday number:  "))
    except ValueError:
        print("Invalid data type!")
        task_1()

    anything_else(task_1)


def task_2():
    """ Задание 2. """

    # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    # Пример:
    # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

    print("GB Python homework. Stage 2. Task 2.")

    try:
        number = int(symbol_request("Please, type in target weekday number:  "))
    except ValueError:
        print("Invalid data type!")
        task_2()

    anything_else(task_2)


def task_3():
    """ Задание 3. """

    # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    # Пример:
    # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

    print("GB Python homework. Stage 2. Task 3.")
    anything_else(task_3)


def task_4():
    """ Задание 4. """

    # Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    # Найдите произведение элементов на указанных позициях.
    # Позиции хранятся в файле file.txt в одной строке одно число.
    # Реализуйте алгоритм перемешивания списка.

    print("GB Python homework. Stage 2. Task 4.")
    anything_else(task_4)


def symbol_request(request):
    symbol = input(str(request))
    return symbol


def anything_else(task):
    print("""
    Do you want anything else?
    Please, type:
    'a' - to start the current task again
    'm' - to get back to the main menu
    'q' - to exit the program
    """)
    again = str(symbol_request("Please, make your choice:  ")).lower()
    match again:
        case 'a':
            task()
        case 'm':
            start_menu()
        case 'q':
            sys.exit()


if __name__ == '__main__':
    start_menu()
