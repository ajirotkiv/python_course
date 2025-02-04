from Tools.scripts.verify_ensurepip_wheels import print_error


class House:
    country = 'LT'
    def __init__(self, price, year):
        self.price = price
        self.year = year

house1 = House(199000, 2025)
house2 = House(65000, 2008)
house1.country = 'LV'
print(
   house1.country, house1.price, house1.year
)
print(
   house2.country, house2.price, house2.year
)


from datetime import datetime

class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        return datetime.today().year - self.year

house_instance_1 = House(10_000_000, 1990)
age = house_instance_1.get_age()
print(age)

house_instance_2 = House(5_000_000, 2001)
age = house_instance_2.get_age()
print(age)

# ===============
class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def __str__(self):
        return f'Namas {self.year} pastatymo, kaina - {self.price}, amzius - {self.get_age()}'

    def get_age(self):
        return datetime.today().year -self.year

# book1 = house(190000, 2024)
# print(book1)
#
# houses = [
#     house(199000, 2025),
#     house(65000, 2008),
#     house(199000, 2025)
# ]
# for house in houses:
#     print(house)
#     print(f'Sena kaina: {house.price}')
#     house.price = round(house.price * 1.22)
houses_kaupiklis = []
while True:
    # quit_choice = input('Iveskite Exit, kad iseiti. Spaskite Enter, kad testi.')
    # if quit_choice == 'exit':
    #     break

    year = int(input('Iveskite metus: '))
    price = int(input('Iveskite kaina: '))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print('Spausdinam ka sukaupem:')
    for house in houses_kaupiklis:
        print(house)


