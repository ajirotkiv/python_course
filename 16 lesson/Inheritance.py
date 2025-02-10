import pickle


class Asmuo:
    def __init__(self, vardas, pavarde, gim_metai):
        self.vardas = vardas
        self. pavarde = pavarde
        self.gim_metai = gim_metai

class MokinioTevas(Asmuo):
    def __init__(self, vardas, pavarde, gim_metai, darbuoviete):
        super().__init__(vardas, pavarde, gim_metai)
        self.darbuoviete = darbuoviete
tevas = MokinioTevas(1, 2, 3, 4)

print(tevas.vardas)
print(tevas.darbuoviete)


class Mygtukas:
    def deaktyvuoti(self):
        print('Mygtukas deaktyvuotas')

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print('Spalva pasikeite i rausva')

red_bnt = RaudonasMygtukas()
red_bnt.deaktyvuoti()

import datetime

class House:
    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year
    def __str__(self):
        return f'Namas {self.year} pastatymo, kaina {self.price}, amzius {self.get_age()}'

try:
    with open('namai.pickle', mode='rb') as f:
        houses_kaupiklis = pickle.load(f)
except:
    houses_kaupiklis = []
while True:
    print('1. Show all houses.')
    print('2. Add house.')
    print('3. Remove last house.')
    print('4. Exit.')
    print('\n')
    try:
        user_input = int(input('Please choose action:'))
        if user_input < 1 or user_input > 4:
            raise ValueError
    except ValueError:
        print('Please choose number from 1 to 4.')
        continue
    if user_input == 4:
        break
    elif user_input == 1:
        for house in houses_kaupiklis:
            print(house)
    elif user_input == 2:
        try:
            price = int(input('Price: '))
            year = int(input('year: '))
            new_house = House(price, year)
            
        except ValueError:
            print('Values shoud be integers')

# new_house = House(190000, 2024)
#
# houses_kaupiklis.append(new_house)
# with open('namai.pickle', mode='wb') as f:
#     pickle.dump(houses_kaupiklis, f)
#
# for h in houses_kaupiklis:
#     print(h)


# with open('info.txt', mode='r') as f:
#     a = f.read()
# print(a)