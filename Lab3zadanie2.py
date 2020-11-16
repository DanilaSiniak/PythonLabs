class Employee:
    name = str()
    def __init__(self):
        print ("Конструктор класса Employee без параметров ", self)
    def __init__(self, name = ""):
        print ("Конструктор класса Employee с параметрами ", self)
        try:
            self.name = name
        except ValueError as error:
            print(error)

    def __del__(self):
        print ("Деструктор класса Employee", self)

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def reading (self):
        try:
            self.name = input("\nВведите актёра: ")
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("\nСотрудник: ", self.name)

class Actor(Employee):
    last_film = str()
    def __init__(self):
        print ("Конструктор класса Actor без параметров ", self)
    def __init__(self, name = "", last_film = ""):
        print ("Конструктор класса Actor с параметрами ", self)
        try:
            self.name = name
            self.last_film = last_film
        except ValueError as error:
            print(error)

    def __del__(self):
        print ("Деструктор класса Actor", self)

    def set_last_film(self, last_film = ""):
        self.last_film = last_film
    def get_last_film(self):
        return self.last_film

    def reading (self):
        try:
            self.name = input("\n Введите актёра: ")
            self.last_film = input(" Введите режиссера ")
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("\n Введите актёра: ", self.name)
        print(" Введите режиссера ", self.last_film, "\n")

class Producer(Actor):
    subordinates = str()
    def __init__(self):
        print ("Конструктор класса Producer без параметров ", self)
    def __init__(self, name = "", last_film = "", subordinates = ""):
        print ("Конструктор класса Producer с параметрами ", self)
        try:
            self.name = name
            self.last_film = last_film
            self.subordinates = subordinates
        except ValueError as error:
            print(error)

    def __del__(self):
        print ("Деструтор класса Producer", self)

    def set_last_film(self, subordinates):
        self.subordinates = subordinates
    def get_last_film(self):
        return self.subordinates

    def reading (self):
        try:
            self.name = input("\n Введите актёра: ")
            self.last_film = input(" Введите режиссера ")
            self.subordinates = input(" Введите сотрудника ")
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("\nВведите актёра: ", self.name)
        print(" Введите режиссера ", self.last_film)
        print(" Введите сотрудника ", self.subordinates, "\n")

employee1 = Employee()
employee1.set_name("Сотрудник1")
employee1.show()

employee2 = Employee("Сотрудник2")
employee2.show()

actor1 = Actor()
actor1.reading()
actor1.show()

actor2 = Actor("Актер2", "Форсаж")
actor2.show()

producer1 = Producer()
producer1.reading()
producer1.show()

producer2 = Producer("Режиссер2", "Гарри Поттер", "Сотрудник1, Сотрудник2, Актер1, Актер2")
producer2.show()
