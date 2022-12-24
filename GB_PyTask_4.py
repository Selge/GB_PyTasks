import random
from GB_PyTask_1 import symbol_request
from GB_PyTask_3 import list_maker


def task_1():
    """ Задание 1. """

#     Вычислить число c заданной точностью d
#     Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

    print("GB Python homework. Stage 4. Task 1.")

def task_2():
    """ Задание 2. """

#     Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    print("GB Python homework. Stage 4. Task 2.")

def task_3():
    """ Задание 3. """

#     Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

    print("GB Python homework. Stage 4. Task 3.")

def task_4():
    """ Задание 4. """

#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#     многочлена и записать в файл многочлен степени k.
#     Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

    print("GB Python homework. Stage 4. Task 4.")


def task_5():
    """ Задание 5. """

#     Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

    print("GB Python homework. Stage 4. Task 4.")


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
#
#
# def list_maker(digit_type):
#     list_len = symbol_request("Please, set the target list length:  ", digit_type)
#     task_list = []
#     for i in range(list_len):
#         task_list.append(random.randint(0, 100))
#     return task_list