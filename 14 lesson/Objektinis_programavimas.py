from Tools.scripts.fixnotice import process

# class House:
#     country = 'LT'
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
# house1 = House(199000, 2025)
# house2 = House(65000, 2008)
# house1.country = 'LV'
# print(
#    house1.country, house1.price, house1.year
# )
# print(
#    house2.country, house2.price, house2.year
# )

# 1. Klasės kūrimas ir statiniai laukai
# Užduotis 1:
# 1. Sukurkite klasę Car, kurioje būtų statinis laukas manufacturer su reikšme
# "Toyota".
# 2. Išveskite manufacturer reikšmę.
# 3. Sukurkite kitą klasę Bike, kurioje būtų statinis laukas manufacturer su reikšme
# "Yamaha" ir taip pat išveskite šią reikšmę.

class Car:
    manufacturer = 'Toyota'

print(
    Car.manufacturer
)

class Bike:
    manufacturer = 'Yamaha'

print(
    Bike.manufacturer
)
print('----------')
# 2. Konstruktorius __init__ ir instancijos laukų inicializavimas
# Užduotis 2:
# 1. Sukurkite klasę Book, kuri turės laukus: title, author, year.
# 2. Naudodami __init__ konstruktorių, inicializuokite šiuos laukus.
# 3. Sukurkite kelias Book instancijas su skirtingais duomenimis.

class Book:
    publisher = "Penguin"
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book('Chacha', 'J. Hadson', 1945)
book2 = Book('Geisha', 'J. Jakudzi', 1990)

print(
   book1.title, book1.author, book1.year
)
print(
   book2.title, book2.author, book2.year
)

print('----------')

# 3. Statinio lauko ir instancijų naudojimas
# Užduotis 3:
# 1. Naudodami klasę Book iš ankstesnės užduoties, išveskite:
# a. Statinį lauką publisher (pridėkite jį kaip "Penguin").
# b. Kiekvienos knygos pavadinimą ir autorių.

print(f'Book Publisher: {Book.publisher}')
print(f'Book name: {book1.title}, author: {book1.author}')
print(f'Book name: {book2.title}, author: {book2.author}')