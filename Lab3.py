class Country:
    count = 0
    country = str()
    population = int()
    square = int()

    def __init__(self):
        Country.count += 1
        print("Количество: ", Country.count)

    def __init__(self, name="", population=0, square=0):
        Country.count += 1
        print("Количество: ", Country.count)
        try:
            self.country = name
            self.population = population
            self.square = square
        except ValueError as error:
            print(error)

    def set_name(self, nameofcountry):
        self.country = nameofcountry

    def set_population(self, population):
        self.population = population

    def set_square(self, square):
        self.square = square

    def get_name(self):
        return self.country

    def get_population(self):
        return self.population

    def get_square(self):
        return self.square

    def reading(self):
        try:
            self.country = input("Введите название страны: ")
            self.population = input("Введите население страны: ")
            self.square = int(input("Введите площадь страны: "))
        except ValueError:
            print("Ошибка ввода")

    def show(self):
        print("\nСтрана: ", self.country, "\nНаселение:", self.population, "\nПлощадь: ", self.square, "\n")


member1 = Country()
member1.set_name("Беларусь")
member1.set_population(9485)
member1.set_square(2075959)
member1.show()

member2 = Country("Россия", 9485, 17100000)
member2.show()

member3 = Country()
member3.reading()
member3.show()
