#Задание 1
def task_1():
    files = os.listdir("D:")
    print ('D:содержит папки: ', files)
    print ('Количество папок: ', len(files))

import os, csv

# вывод списка на консоль
def output(arr):
    for i in arr:
        for j in range(len(i)):
            print(i[j], end=" ")
        print()
    print()

# ввод списка в excel

# чтение из файла (задание 5)
def reader():
    f = open("D:\students.csv", "r")
    reader = csv.reader(f)
    arr = []
    for i in reader:
        arr.append(str(i)[2:len(i) - 3].split(';'))
    f.close()
    print("Исходные данные: ", arr, "\n")
    output(arr)
    return arr


# запись в файл (задания 4, 5)
def writer(arr):
    f = open("D:\students.csv", "w", newline="")
    writer = csv.writer(f)
    for i in arr:
        line = [';'.join(i)]
        writer.writerow(line)
    f.close()


# Задание 2
def sort_col(i):
    return i[2]


def task_2():
    print("Задание 2.")
    students = reader()

    students.sort(key=sort_col)
    print("Отсортированный список: ", students, "\n")

    output(students)
    writer(students)
    students.clear


# Задание 3
def task_3():
    print("Задание 3.")
    students = reader()

    num_group = input("Введите номер группы: ")
    for i in range(len(students)):
        if students[i][3] == num_group:
            students[i][2] = str(int(students[i][2]) + 1)
    print("\nНовый список: ", students, "\n")

    output(students)
    writer(students)
    students.clear

def task_4():
    import os
    import time
    path = 'D:\KyrsovayaRabota\js\style.txt'
    isFile = os.path.isfile(path)
    print(isFile)





def menu():
    num_task = -1
    while (num_task != 0):
        print("0 - Выход")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3\n")
        print("4 - доп задание")
        print("5 - доп задание")
        num_task = int(input("Введите номер задания: "))
        if num_task == 1:
            task_1()
        elif num_task == 2:
            task_2()
        elif num_task == 3:
            task_3()
        elif num_task == 4:
            task_4()
        elif num_task == 5:
            task_5()
        elif num_task == 6:

            print("Вы ввели неправильный номер задания")

        if (input("Хотите продолжить? (+/-)\n") == '-'):
            break;
        print()


menu()
