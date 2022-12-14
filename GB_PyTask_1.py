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
    task_pointer = str(input("Please, make your choice:  "))
    match task_pointer:
        case '1':
            task_1()
        # case '2':
        #     task_2()
        # case '3':
        #     task_3()
        # case '4':
        #     task_4()
        # case '5':
        #     task_5()
        case 'q':
            print("Well, see ya later. Bye!")
            sys.exit()
        case _:
            print("Please, use built-in options!")
            match_pointer()


def task_1():
    print("""GB Python homework. Stage 1. Task 1.
    Задание 1.
    Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
    является ли этот день выходным.
    
    Пример:
    - 6 -> да
    - 7 -> да
    - 1 -> нет
    """)

    weekdays = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
    day = int(input("Please, type in target weekday number:  "))

    if 5 >= day >= 1:
        print(f"No, {weekdays[day - 1]} (day {day}) is not a weekend. It's a business day, get back to work!")
    elif 7 >= day >= 6:
        print(f"Yes, {weekdays[day - 1]} (day {day}) is a weekend. Have some rest!")
    else:
        print("Wrong day number! Use numbers in range 1 - 7!")

    something_else()


def task_2():
    pass


def task_3():
    pass


def task_4():
    pass


def task_5():
    pass


if __name__ == '__main__':
    start_menu()

#   Задание 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
#  Задание 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
#     Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#
#  Задание 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#
#  Задание 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
#     Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
