from math import *
# Задание 1
def task_1_1():


    print ("<---------------------------Задание 1-------------------------------------->")
    print ("Напишите программу для решения примера (по вариантам). Пример берётся по |модулю|. ")
    print ("Все необходимые переменные пользователь вводит через консоль")
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    d = int(input("Введите d: "))
    k = int(input("Введите k: "))

    if a == 0 or b == 0 or k == 0 or c == 0 or d == 0:
       print("Делить на ноль нельзя .")
    else:
        res = fabs((((a ** 2 / b ** 2) + c ** 2 * a ** 2) / (a + b + c * (k - a/(b ** 3))))
                   + c + ((k / b) - (k / a)) * c)
        # fabs - модуль
        print("Результат: ", res)

def task_1_2():
    print ("<---------------------------Задание 2-------------------------------------->")
    print("Дан произвольный список, содержащий и строки, и числа. Выведите все четные элементы построчно")
    print("Введите произвольный список:" )
    list = ["rwq", 31, 32, "ads", 54,"123",23]
    k = 0
    print("Список ", list)
    while k < len(list):
        if k % 2 == 1:
            print("Элемент -", list[k], "четный" )
        k += 1

def task_1_3(numbers):
    print ("<---------------------------Задание 3-------------------------------------->")
    print ("Дан произвольный список, содержащий только числа. Выведите результат сложения всех больше 10")
    print ("Список: ", numbers)
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    sum = 0
    for i in range(len(numbers)):
        if (numbers[i] >= 10 and numbers[i] != 10):
            sum += numbers[i]
    print("Сумма: ", sum)

def task_1_4(numbers):
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("<---------------------------Задание 4-------------------------------------->")
    print("Дан произвольный список, содержащий только числа. Выведите максимальное число")
    print("Список: ", numbers)
    print("Максимальные эелемент: ", max(numbers))
########################################################################################################################
#Задание 2

# ЗАДАНИЕ 2
def task_2_1():
    print("Задание 1")
    print("Пусть задано некоторое число my_number. Пользователь вводит с клавиатуры свое число user_number.")
    print("Пользователь вводит с клавиатуры свое число user_number.")
    print("Запрашивайте у пользователя вводить число user_numder до тех пор, пока оно не меньше числа my_number.")
    my_number = 5
    print("Число для сравнения", my_number)
    user_number = int(input("Введите число: "))
    while (my_number <= user_number):
        user_number = int(input("Введите число (цикл остановится, когда введёте число меньше 5): "))


def task_2_2():
    print("Задание 2")
    print("Пусть дан список, содержащий строки. Выведите построчно все строки размером от 5 до 10 символов.")

    list = ["dfghf6", "udwfigegrf", "urff", "dhfgeuiyfuigeigrhfi", "qwerty"]
    print("Список: ", list)
    for i in range(len(list)):
        if (len(list[i]) >= 5 and len(list[i]) <= 10 ):
            print(list[i])
    list.clear


import random
from random import choice
from string import ascii_uppercase


def task_2_3():
    print("Задание 3")
    print("Сгенерируйте и выведите случайную строку, состоящую из 5 символов, содержащую только заглавные буквы русского алфавита")
    str = ""
    for i in range(5):
        str += choice(ascii_uppercase)
    print(str)


def task_2_4():
    print("Задание 4")
    print("Дана строка. На основе данной строки сформулируйте новую, содержащую только цифры.")
    stroka = "3fwk5kf53a23wkf24kfa54wf2"
    print("Исходная строка: ", stroka)
    new_stroka = ""
    for k in range(len(stroka)):
        if (stroka[k].isdigit()):
            new_stroka += stroka[k]
    print("Строка без цифр: ", new_stroka)
    print()

#ЗАДАНИЕ 3
def task_3_1(matr, size_str, size_col):
    print ("Задание 1")
    print ("Напишите функцию возведения всех элементов элементов в квадрат.")
    for i in range(size_str):
        for j in range(size_col):
            if(matr[i][j]):
                matr[i][j] = int(matr[i][j] ** 2)
            print(matr[i][j], end = " ")
        print()

def task_3_2(matr, size_str, size_col):
    print("Задание 2")
    print("Напишите функцию сложения по строкам.")
    sum_stroka = []
    for i in range(size_col):
        for j in range(size_str):
            sum_stroka.append(0)
            sum_stroka[j] += matr[j][i]

    for i in range(size_col):
        print(sum_stroka[i])
    print()


def task_3_3(matr, size_str, size_col):
    print("Задание 3")
    print("Напишите функцию умножение строкам.")
    sum_stroka = []
    for i in range(size_col):
        for j in range(size_str):
            sum_stroka.append(1)
            sum_stroka[j] *= matr[j][i]

    for i in range(size_col):
        print(sum_stroka[i])
    print()


def task_3_4(matr, size_str, size_col):
    print ("Задание 4")
    print ("Пользователь вводит через консоль число. Напишите функцию, замены всех четных числ матрицы на 0")
    number = 0
    for i in range(size_str):
        for j in range(size_col):
            if(matr[i][j] % 2 == 0):
                matr[i][j] = number
            print(matr[i][j], end = " ")
        print()




def task_3_5(matr, size_str, size_col):
    print("Задание 5")
    print("Пользователь вводит через консоль число. Напишите функцию удаления столбца в матрице, чей номер равен"
          " введенному числу.")
    num_stolb = int(input("Введите число: "))
    for i in range(size_str):
        for j in range(size_col):
            if (j == num_stolb):
                del (matr[i][j])
    size_col -= 1

    print()
    for i in range(size_str):
        for j in range(size_col):
            print(matr[i][j], end=" ")
        print()



def task_3_6():
    print ("Задание 6")
    print ("Напишите функцию создания матрицы любого размера, заполненного нулями.")
    N = int(input("Введите количество строк: "))
    M = int(input("Введите колиество столбцов: "))
    arr = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            print (arr[i][j], end =" ")
        print ()
    arr.clear

def task_3_7(matr, size_str, size_col):
    print ("Задание 7")
    print ("Пусть пользователь через консоль вводит число: номер строки.")
    print ("Напишите функцию, которая выведет все элементы данной строки, возведенные в квадрат")
    number = int(input("Введите номер строки: "))
    for i in range(size_str):
        if i == number + 1:
            for j in range(size_col):
                print (int(matr[i][j] ** 2), end =" ")

# ЗАДАНИЕ 4

def task_4_1():
    print("Задание 1")
    print("Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На основании этой строки создайте ")
    print("Содержащую только слова больше 5 символов. Разделитель слов в строке - пробел")

    list = ["dfghf6", "udwfigegrf", "urff", "dhfgeuiyfuigeigrhfi", "qwerty"]
    print("Список: ", list)
    for i in range(len(list)):
        if (len(list[i]) >= 5):
            print(list[i], end = " ")
    list.clear


def task_4_2():
    print("Задание 2")
    print("Пусть дана строковая переменная, содержащая информацию о студентах. Выведите информацию в виде:")
    my_string = "Фамилия;Имя;Отчество;Возраст;Категория;Иванов;Иван;Иванович;"
    "23 года;""Cтудент 3 курса;Петров;Семен;Игоревич;22 года;Cтудент 2 курса"
    my_string = my_string.split(';')
    for i in range(len(my_string)):
        print(my_string[i].ljust(10), end=" ")
        if (i + 1) % 5 == 0:
            print()


def task_4_3():

    print("Задание 3")
    print("Пусть дана строковая переменная: Выведите построчно информацию о студентах, чей возраст больше «21 года».")

    my_string = (
        "Фамилия;Имя;Отчество;Возраст;Категория;Иванов;Иван;Иванович;23 года;"
        "Cтудент 3 курса;Петров;Семен;Игоревич;22 года;Cтудент 2 курса;")
    my_string = my_string.split(';')
    for i in range(len(my_string)):
        print(my_string[i].ljust(10), end=" ")
        if (i + 1) % 5 == 0:
            print()


def task_4_4():
    print("Задание 4")
    print('Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов. ')
    print('Результат:')
    my_string = 'Раз два три четыре пять'
    print("Строка: ", my_string)
    print("Длина строки: ", len(my_string), "Количество слов: ", len(my_string.split()))

#Задание 5

def task_5_1():
    print ("Задание 1")
    print ("Пусть дана матрица чисел размером NxN. Представьте данную матрицу в виде списка."
           " Выведите результат сложения всех элементов матрицы")
    N = 5
    matr = [[1,2,3,4,5],
            [8,7,6,5,4],
            [2,3,4,5,6],
            [9,8,7,6,5],
            [1,3,5,7,9]]
    list = []
    print("Матрица: ")
    for i in range(N):
        for j in range(N):
            print(matr[i][j], end = ' ')
            list.append(matr[i][j])
        print()
    print("Список: ", list)
    sum = 0
    for i in list:
        sum += list[i]
    print("Сумма: ", sum)
    list.clear
    matr.clear

def task_5_2():
    print ("Задание 2")
    print ("Пусть дан список на 10 элементов. Удалите все четные элементы и добавьте 2 новых."
           " Выведите список на экран.")
    N = 10
    list = []
    for i in range(N):
        list.append(i)
    print("Исходный список: ", list)

    j = 0
    for i in range(len(list)):
        if ((i + 1) % 2 == 0):
            list.pop(j)
            j -= 1
        j += 1
    print("Удалила элементы с четным индексом: ", list)

    list.append(2233)
    list.append(9012)
    print("Добавила еще 2 элемента: ", list)
    list.clear

def task_5_3(my_len):
    print ("Задание 3")
    print ("Пусть журнал по предмету «Информационные технологии» представлен."
           " Выведите список студентов конкретной группы в одной строке.")
    for i in range(len(my_len)):
        print (my_len[i][0], end=" "*(15-len(my_len[i][0])))
        for j in range (len(my_len[i][1])):
            print (my_len[i][1][j], end = " "*(20-len(my_len[i][1][j])))
        print()

def task_5_4(my_len):
    print ("Задание 4")
    print ("Пусть журнал по предмету «Информационные технологии» представлен из прошлого задания.")
    print ("Выведите всех студентов и их группы, чья фамилия меньше 7 букв:")
    for i in range(len(my_len)):
        for j in range (len(my_len[i][1])):
            if(len(my_len[i][1][j].split(' ', 1)[0]) < 7):
                print (my_len[i][1][j])

def menu():
    num_task = -1
    while (num_task != 0):
        print("0 - Выход")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3")
        print("4 - Задание 4")
        print("5 - Задание 5")
        num_task = int(input("Введите номер задания: "))
        if num_task == 1:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            task_1_1()
            task_1_2()
            task_1_3(numbers)
            task_1_4(numbers)
            numbers.clear
        elif num_task == 2:
            task_2_1()
            task_2_2()
            task_2_3()
            task_2_4()
        elif num_task == 3:
            size_col = 8
            size_str = 8
            matr = [[1,2,3,4,5,6,7,8],
                [8,7,6,5,4,3,2,1],
                [2,3,4,5,6,7,8,9],
                [9,8,7,6,5,4,3,2],
                [1,3,5,7,9,7,5,3],
                [3,1,5,3,2,6,5,7],
                [1,7,5,9,7,3,1,5],
                [2,6,3,5,1,7,3,2]]
            task_3_1(matr,size_str,size_col)
            task_3_2(matr,size_str,size_col)
            task_3_3(matr,size_str,size_col)
            task_3_4(matr,size_str,size_col)
            task_3_5(matr,size_str,size_col)
            task_3_6(matr,size_str,size_col)
            task_3_7(matr, size_str, size_col)

            matr.clear
        elif num_task == 4:

            task_4_1()
            task_4_2()
            task_4_3()
            task_4_4()
        elif num_task == 5:
            task_5_1()
            task_5_2()
            my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']], ['БО-421102',['ляля яна', 'тартата трр']],['БО-331103',['твотл ва', 'вама ва', 'роа ира']]]
            task_5_3(my_len)
            task_5_4(my_len)
            my_len.clear
        else:
            print("Вы ввели неправильный номер задания")

        if (input("Хотетите продолжить? (+/-)\n") == '-'):
            break

menu()
