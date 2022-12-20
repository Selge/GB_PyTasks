from GB_PyTask_1 import symbol_request


def task_1():
    """ Задание 1. """

    # 1. Задайте список из нескольких чисел.
    #    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    #    Пример:
    # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

    print("GB Python homework. Stage 3. Task 1.")


def task_2():
    """ Задание 2. """

    # 2. Напишите программу, которая найдёт произведение пар чисел списка.
    #    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    #    Пример:
    # - [2, 3, 4, 5, 6] => [12, 15, 16];
    # - [2, 3, 5, 6] => [12, 15]

    print("GB Python homework. Stage 3. Task 2.")


def task_3():
    """ Задание 3. """

    # 3. Задайте список из вещественных чисел.
    #    Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    #     Пример:
    # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    print("GB Python homework. Stage 3. Task 3.")


def task_4():
    """ Задание 4. """

    # 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    #    Пример:
    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

    print("GB Python homework. Stage 3. Task 4.")


def task_5():
    """ Задание 5. """

    # 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    #    Пример:
    # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    # [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

    print("GB Python homework. Stage 3. Task 5.")


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
