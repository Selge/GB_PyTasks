import random

from GB_PyTask_1 import symbol_request


def list_maker(digit_type):
    list_len = symbol_request("Please, set the target list length:  ", digit_type)

    task_list = [random.randint(0, 100) for _ in range(list_len)]

    return task_list


def task_1():
    """ Задание 1. """

    # 1. Задайте список из нескольких чисел.
    #    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    #    Пример:
    # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

    print("GB Python homework. Stage 3. Task 1.")

    task_list = list_maker(int)

    summary = 0

    for i in range(len(task_list)):
        if i % 2 != 0:
            summary += task_list[i]

    print(f"Your list is: {task_list}, odd places sum is: {summary}")


def task_2():
    """ Задание 2. """

    # 2. Напишите программу, которая найдёт произведение пар чисел списка.
    #    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    #    Пример:
    # - [2, 3, 4, 5, 6] => [12, 15, 16];
    # - [2, 3, 5, 6] => [12, 15]

    print("GB Python homework. Stage 3. Task 2.")

    pairs = list_maker(int)

    if len(pairs) % 2 == 0:
        pair = len(pairs) // 2
    else:
        pair = len(pairs) // 2 + 1

    results = []

    for i in range(pair):
        results.append(pairs[i] * pairs[len(pairs) - i - 1])

    print(f"Your income list is: {pairs}, outcome list sum is: {results}")


def task_3():
    """ Задание 3. """

    # 3. Задайте список из вещественных чисел.
    #    Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    #     Пример:
    # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    print("GB Python homework. Stage 3. Task 3.")

    list_len = symbol_request("Please, set the target list length:  ", int)

    third_list = []

    for i in range(list_len):
        third_list.append(round(random.uniform(00.01, 99.99), 2))

    cut_list = []

    for e in third_list:
        cut = str(e)[str(e).find(".") + 1:]
        if len(cut) < 2:
            cut_list.append((int(cut)) * 10)
        else:
            cut_list.append(int(cut))

    result = max(cut_list) - min(cut_list)

    print(f"Your incoming list:  {third_list}. Fractional difference: {result}.")


def task_4():
    """ Задание 4. """

    # 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    #    Пример:
    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

    print("GB Python homework. Stage 3. Task 4.")

    number = symbol_request("Please, enter target number:  ", int)

    print(f"Your number is: {number}, your binary number is: {number: b}.")


def task_5():
    """ Задание 5. """

    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # Пример:
    # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

    print("GB Python homework. Stage 3. Task 5.")

    number = symbol_request("Please, enter target number:  ", int)

    print(f"Fibonacci list for {number} is:  {fibonacci(number)}.")


def fibonacci(n):

    pos_arr = [0] * (n + 1)
    neg_arr = [0] * n
    pos_arr[1] = neg_arr[-1] = 1

    for i in range(2, (n + 1)):
        pos_arr[i] = pos_arr[i-1] + pos_arr[i-2]
        neg_arr[-i] = neg_arr[-i + 2] - neg_arr[-i + 1]

    fibo_arr = neg_arr + pos_arr

    return fibo_arr


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
