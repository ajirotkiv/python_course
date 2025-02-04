from Tools.scripts.fixnotice import process


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
    publisher = "Penguin" #statinis laukas
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

print(f'Book name: {book1.title}, Author: {book1.author} Publisher: {Book.publisher}')
print(f'Book name: {book2.title}, Author: {book2.author} Publisher: {Book.publisher}')

print('---------------')
# 4. Klasės instancijų atvaizdavimas
# Užduotis 4:
# 1. Išveskite bet kurią Book instanciją naudojant print().
# 2. Pastebėkite rezultatą (turėtų būti atminties adresas).

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title  = title
        self.author = author
        self.year = year

    def get_age(self):
        return datetime.today().year - self.year

book_instance_1 = Book('Geisha', 'J. Jakudzi', 1990)
book_instance_2 = Book('Chacha', 'J. Hadson', 1945)
age = book_instance_1.get_age()
age2 = book_instance_2.get_age()
print(book_instance_1)

print('---------------')
# 5. Savų metodų kūrimas klasėje
# Užduotis 5:
# 1. Pridėkite metodą get_book_age(), kuris grąžins, kiek metų praėjo nuo knygos
# išleidimo.
# 2. Sukurkite kelias knygas ir iškvieskite šį metodą.

print(f'Book name: {book1.title}, Author: {book1.author} Book age: {age}')
print(f'Book name: {book2.title}, Author: {book2.author} Book age: {age2}')

print('---------------------')

# Užduotis 6:
# 1. Sukurkite Book instanciją ir naudokite get_book_age() metodą.
# 2. Išveskite rezultatą kartu su pranešimu:
# "Knyga <pavadinimas> yra <amžius> metų senumo."

book_instance_1 = Book('Chacha', 'J. Hadson', 1945)
age = book_instance_1.get_age()
print(f'Knyga {book2.title} yra {age} metu senumo')