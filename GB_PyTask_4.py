import random
import itertools

from GB_PyTask_1 import symbol_request
from GB_PyTask_3 import list_maker


def task_1():
    """ Задание 1. """

# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

    print("GB Python homework. Stage 4. Task 1.")

    number = symbol_request("Please, set the target number:  ", float)

    def calc_pi(eps=1.0e-5):
        s = 0
        d = 1
        sgn = 1
        while True:
            a = 4 / d
            s = s + sgn * a
            if a < eps:
                return s
            sgn = -sgn
            d = d + 2

    print(calc_pi())

def task_2():
    """ Задание 2. """

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    print("GB Python homework. Stage 4. Task 2.")

    number_1 = number_2 = symbol_request("Please, set the target number:  ", int)
    i = 2
    list_2 = []

    while i * i <= number_2:
        while number_2 % i == 0:
            list_2.append(i)
            number_2 = number_2 / i
        i = i + 1
    if number_2 > 1:
        list_2.append(number_2)

    print(f"Your number is: {number_1}. The list of prime factors for {number_1} is {list_2}.")


def task_3():
    """ Задание 3. """

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

    print("GB Python homework. Stage 4. Task 3.")

    numbers = list_maker(int)
    uniq_numbers = set(numbers)

    print(f"Your incoming list is: {numbers}.\nThe outcoming list is: {uniq_numbers}.")


def task_4():
    """ Задание 4. """

#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#     многочлена и записать в файл многочлен степени k.
#     Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

    print("GB Python homework. Stage 4. Task 4.")

    k = symbol_request("Please, set the target number:  ", int)
    task_list = [random.randint(0, 101) for _ in range(k + 1)]

    polynome = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(task_list) if j][::-1]) + ' = 0'
    polynome += ('', '1')[polynome[-1] == '+']
    polynome = (polynome, polynome[:-2])[polynome[-2:] == '^1']
    polynome = polynome.replace('x^1+', 'x+')
    polynome = polynome.replace('x^0', '')

    return polynome


def task_5():
    """ Задание 5. """

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

    print("GB Python homework. Stage 4. Task 4.")
    #
    # polynom_1 = task_4()
    # polynom_2 = task_4()

    # with open("file.txt", "r") as file:

    # нахождение суммы многочлена

    with open('file34_1.txt', 'r') as data:
        st1 = data.readlines()
    with open('file34_2.txt', 'r') as data:
        st2 = data.readlines()
    print(f"Первый многочлен {st1}")
    print(f"Второй многочлен {st2}")
    lst1 = calc_mn(st1)
    lst2 = calc_mn(st2)
    ll = len(lst1)
    if len(lst1) > len(lst2):
        ll = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(ll)]
    if len(lst1) > len(lst2):
        mm = len(lst1)
        for i in range(ll, mm):
            lst_new.append(lst1[i])
    else:
        mm = len(lst2)
        for i in range(ll, mm):
            lst_new.append(lst2[i])
    write_file("file34_res.txt", create_str(lst_new))
    with open('file34_res.txt', 'r') as data:
        st3 = data.readlines()
    print(f"Результирующий многочлен {st3}")

    # разбор многочлена и получение его коэффициентов

    def calc_mn(st):
        st = st[0].replace(' ', '').split('=')
        st = st[0].split('+')
        lst = []
        l = len(st)
        k = 0
        if sq_mn(st[-1]) == -1:
            lst.append(int(st[-1]))
            l -= 1
            k = 1
        i = 1  # степень
        ii = l - 1  # индекс
        while ii >= 0:
            if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
                lst.append(k_mn(st[ii]))
                ii -= 1
                i += 1
            else:
                lst.append(0)
                i += 1

        return lst

    # получение степени многочлена
    def sq_mn(k):
        if 'x^' in k:
            i = k.find('^')
            num = int(k[i + 1:])
        elif ('x' in k) and ('^' not in k):
            num = 1
        else:
            num = -1
        return num

    # получение коэффицента члена многочлена

    def k_mn(k):
        if 'x' in k:
            i = k.find('x')
            num = int(k[:i])
        return num

def data_record():
    ...


def data_read():
    ...


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


#def list_maker(digit_type):
#   list_len = symbol_request("Please, set the target list length:  ", digit_type)
#
#   task_list = [random.randint(0, 100) for _ in range(list_len)]
#
#   return task_list


if __name__ == '__main__':
    task_4()
