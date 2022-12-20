from GB_PyTask_1 import symbol_request


def task_1():
    """ Задание 1. """

    #  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    #  Пример:
    # - 6782 -> 23
    # - 0,56 -> 11

    print("GB Python homework. Stage 2. Task 1.")

    try:
        number = float(symbol_request("Please, type in target value:  "))
    except ValueError:
        print("Invalid data type!")
        task_1()


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



def task_3():
    """ Задание 3. """

    # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    # Пример:
    # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

    print("GB Python homework. Stage 2. Task 3.")


def task_4():
    """ Задание 4. """

    # Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    # Найдите произведение элементов на указанных позициях.
    # Позиции хранятся в файле file.txt в одной строке одно число.
    # Реализуйте алгоритм перемешивания списка.

    print("GB Python homework. Stage 2. Task 4.")
