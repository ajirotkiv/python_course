# def sudeti_skaicius(*args):
#     return sum(args)
#
# print(sudeti_skaicius(5, 10, 15))
# print(sudeti_skaicius(100, 200, 300, 400))
#
# def sveikiti_vardus(*args):
#    res = ''
#    for name in args:
#         print(f'Labas, {name}')
# sveikiti_vardus('Jonas', 'Petras', "Bronius")
#
#
# def spausdinti_zinutes(kartai, *args, pabaiga = "!"):
#     for elem in args:
#         print(elem * kartai, pabaiga)
# spausdinti_zinutes(5, 'Hi! ', 'Bounjour ', 'Labas ', pabaiga= ':-)')
#
# print('---------------')
#
# def dauginti_skaicius(n, *args):
#     for i in args:
#         print((i + ' ')* n)
# dauginti_skaicius(3, 'Sunday', 'Mondey', 'Wednesdey')
#
#
from logging import exception


# kwargs
# def rodyti_duomenis(**kwargs):
#     print(kwargs)
# rodyti_duomenis(pirmas =1, antras = 2, trecias = 3)
#

# funkcija registruoti naudotoja
# def registruoti_naudotoja(vardas, e_pastas, **kwargs):
#     for user in kwargs:
#         print(vardas, e_pastas, **kwargs)
# vardas = ['Boris', 'John', 'Peter']
# e_pastas = ['gg@ff.lt', 'tt@kf.lt', 'ee@lf.lt']
# registruoti_naudotoja(vardas, e_pastas, end='!\n')
#
# def atspausdinti_lista(listas, **kwargs):
#     for item in listas:
#         print(item, **kwargs)
# list_dom = ['Sunday', 'Monday', 'Thursday', 'Wednesday', 'Thirsday', 'Friday', 'Saturday']
# atspausdinti_lista(list_dom, sep = "---", end = "\n")

#
# def kelk_laipsniu(sk, laipsnis = 2, **kwargs):
#     res = sk ** laipsnis
#     return res
# print(kelk_laipsniu(2, laipsnis=3, radianas=2))


# lambda
# def grazink_index_1(listas):
#     return listas[1]
# darbuotojai = [
#     ['Valdas', 'programuotojas', 2000],
#     ['Adomas', 'direktorius', 3000],
#     ['Aldona', 'vadybininkas', 1800],
#     ['Jogaila', 'programuotojas', 2500],
# ]
# res = sorted(darbuotojai, key=grazink_index_1)
# res = sorted(darbuotojai, key=lambda listas:[1])
# # res = sorted(darbuotojai)
# print(res)

# lambda argumentai: israiska
# def sudeti(a, b):
#     return a + b
# print(sudeti(3, 5))
# sudeti_lambda = lambda a, b: a + b
# print(sudeti_lambda(3, 5))
#
# skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# lyginiai_skaiciai = list(filter(lambda  x: x % 2 == 0, skaiciai))
# print(lyginiai_skaiciai)

# print((lambda a: a**2)(5))
#
# darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
# print(sorted(darbuotojai, key = lambda x: x[1]))
#
#
# sarasas = [5, 10, 15, 20, 25, 30]
# print(list(filter(lambda x: x % 10 == 0, sarasas)))


# try - except
#
# def dalinti(a,b):
#     try:
#         return a / b
#     except exception as e:
#         return 'Dalyba is nulio negalima'
#
# print(dalinti(10, 2))
#
# dalinti = lambda a, b: a/5


num1 = input('Iveskite pirma skaiciu: ')
num2 = input('Iveskite antra skaiciu: ')
try:
    num1 = int(num1)
    num2 = int(num2)
    res =  num1 / num2
    print(res)
except ValueError:
    print('Turi buti iveskas skaicius!')

except ZeroDivisionError:
    print('Dalyba is nulio negalima. Iveskite kita skaiciu')
