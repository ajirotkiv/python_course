# name  = 'Natusik'
# def create_greetings(user):
#     res = f'Greetings, {user}'
#     return res
# print(
#     create_greetings('name')
# )

# def sudaugink(num1, num2):
#     res = num1 * num2
#     return res
# res = sudaugink(5, 10)
# print(f'Dvieju skaiciu sandauga: ', res)
# sudaugink(5, 10)


# mokytojo kodas
# def sudaugink(x, y):
#     if not x or not y:
#         return
#     return  x * y
# suma = sudaugink(5, 10)
# if suma:
#     print(suma)
# else:
#     print('Numbers are wrong or not provided')


# def greet(name = 'Jim'):
#     print(f'Hello, {name}!')
#
# greet('Darius')
# greet()
#
# def priimk_pacienta(pacientas, gydytojas = 'gyd. Pagalnutylenis'):
#     irasas_gydytojo_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
#     return irasas_gydytojo_zurnale
#
# res = priimk_pacienta('Adomas')
# print(res)
#
# res = priimk_pacienta('Rolandas')
# print(res)
#
# res = priimk_pacienta('Adomas', gydytojas='gyd. BBBBB')
# print(res)

# Užduotis 3:
# Sukurkite funkciją trys_sveikinimai(vardas1, vardas2, vardas3), kuri priimtų tris
# vardus ir kiekvienam iš jų atspausdintų pasisveikinimą.
# Pvz.: „Labas, Jonas!“, „Labas, Asta!“, „Labas, Mantas!“.
# 4. Numatytosios reikšmės ir keyword argumentai
# user = ''
# def trys_sveikinimai(vardas1, vardas2, vardas3):
#     greetings = f'Labas, {vardas1}', f'Labas, {vardas2}', f'Labas, {vardas3}'
#     return greetings
# res = trys_sveikinimai('Adomas', 'Petras', 'Jurate')
# print(res)
#

# Užduotis 4:
# Sukurkite funkciją sveikink_su_pavadinimu(vardas, pavadinimas="drauge"), kuri
# atspausdintų žinutę: „Sveikas, [vardas]! Ką veiki, [pavadinimas]?“.
# 1. Iškvieskite funkciją nenurodydami pavadinimo.
# 2. Iškvieskite funkciją, nurodydami pavadinimą „kolega“.

# def sveikink_su_pavadinimu(vardas, pavadinimas="drauge"):
#     print(f'Sveikas, {vardas}! Ka veiki, {pavadinimas}?')
# sveikink_su_pavadinimu('Bernotas')
# sveikink_su_pavadinimu('Lukas', 'kaimine')
#
#

# Loginiai jungikliai funkcijose
# Užduotis 5:
# Sukurkite funkciją skaiciuoti_sumos_tipą(x, y, tik_teigiama=False), kuri
# priimtų du skaičius ir grąžintų jų sumą.
# • Jei tik_teigiama=True, funkcija grąžintų tik teigiamą sumą (jei suma neigiama,
# grąžintų 0).

# def skaiciuoti_sumos_tipą(x, y, tik_teigiama=False):
#     if not tik_teigiama:
#         return 0
#     else:
#         return x + y
#
# print(skaiciuoti_sumos_tipą(6, 8, True))
# print(skaiciuoti_sumos_tipą(-6, 8, False))

# Docstringai funkcijose
# Užduotis 6:
# Sukurkite funkciją apskaiciuok_vidurki(skaiciai), kuri apskaičiuotų ir grąžintų
# sąrašo skaičių vidurkį. Pridėkite docstring su informacija apie:
# • Funkcijos paskirtį.
# • Argumentus (sąrašas skaičių).
# • Grąžinamą reikšmę (vidurkis).

# def apskaiciuok_vidurki(skaiciai):

# Type hints ir anotacijos

# Užduotis 7:
# Sukurkite funkciją prideti_zodi(tekstas: str, zodis: str) -> str, kuri priimtų
# sakinį ir pridedamą žodį, o tada grąžintų sakinį su tuo žodžiu gale.

# from Lib import matematika

# print(matematika.sudetis(4, 7))
# print(matematika.daugyba(1, 8))

from moduliai import aritmetika
from moduliai.aritmetika import atimtis

print(aritmetika.atimtis(10, 7))
print(aritmetika.dalyba(10, 5))

import moduliai.aritmetika
print((moduliai.aritmetika.atimtis(20, 5)))
print((moduliai.aritmetika.dalyba(10, 2)))

from moduliai.aritmetika import atimtis, dalyba
print(aritmetika.atimtis(50, 25))
print(aritmetika.dalyba(100, 4))

import moduliai.aritmetika as ar
print(ar.atimtis(30, 10))
print(ar.dalyba(50, 5))

import moduliai
print(moduliai.aritmetika.atimtis(15, 5))
