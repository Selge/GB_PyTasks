import random
import math
from random import shuffle
from GB_PyTask_1 import symbol_request


def task_1():
    """ Задание 1. """

    #  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    #  Пример:
    # - 6782 -> 23
    # - 0,56 -> 11

    print("GB Python homework. Stage 2. Task 1.")

    number = symbol_request("Please, type in target value:  ", float)
    print(sum(map(int,str(str(number).replace('.', '')))))


def task_2():
    """ Задание 2. """

    # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    # Пример:
    # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

    print("GB Python homework. Stage 2. Task 2.")

    number = symbol_request("Please, type in target number:  ", int)
    factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

    result = []
    for i in range(1, number + 1):
        result.append(factorial(i))

    print(result)


def task_3():
    """ Задание 3. """

    # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    # Пример:
    # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

    print("GB Python homework. Stage 2. Task 3.")

    n = symbol_request("Please, set up target number:  ", int)
    n_dict = {}
    n_list = []
    for i in range(1, n + 1):
        n_dict[i] = round(((1 + 1 / i) ** i), 2)
        n_list.append(n_dict[i])
    print(f"Sequence: {n_dict}\nSum:  {sum(n_list)}")


def task_4():
    """ Задание 4. """

    # Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    # Найдите произведение элементов на указанных позициях.
    # Позиции хранятся в файле file.txt в одной строке одно число.

    print("GB Python homework. Stage 2. Task 4.")
    # Получаем желаемый список.
    n = symbol_request("Please, set up the target value:  ", int)
    n_list = []
    for e in range(n + 1):
        e = random.randint(-n, n + 1)
        n_list.append(e)
    print(f"Our list: {n_list}")

    # Получаем набор позиций в списке. Я взял четверть всех позиций списка (чтоб было интереснее), поэтому 4
    #  Здесь можно было наверное упростить, но я использовал множество, чтобы избежать повторения позиций элементов.
    positions = set()
    for g in range(round(len(n_list) / 4)):
        g = random.randint(0, len(n_list) - 1)
        positions.add(g)
    # Записываем позиции в файл построчно
    with open(r"file.txt", "w") as file:
        for i in positions:
            file.write(f"{i}\n")

    # Читаем позиции из файла и получаем произведение чисел, стоящих на указанных местах:
    total = 1
    with open(r"file.txt", "r") as file:
        for line in file:
            total *= n_list[int(line)]
    print(f"Total: {total:,.0f}".replace(',', ' '))


def task_5():
    """ Задание 5. """

    # Реализуйте алгоритм перемешивания списка.

    print("GB Python homework. Stage 2. Task 5.")




# In case import doesn't work, please, uncomment the code below, and you'll be all set:
# def symbol_request(request, datatype):
#     request = request
#     datatype = datatype
#     try:
#         symbol = datatype(input(request))
#     except ValueError:
#         print("Invalid data type!")
#         symbol_request(request, datatype)
#
#     return symbol

if __name__ == '__main__':
    task_4()
