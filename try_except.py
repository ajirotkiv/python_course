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

#
# num1 = input('Iveskite pirma skaiciu: ')
# num2 = input('Iveskite antra skaiciu: ')
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     res =  num1 / num2
#     print(f'Resultatas: {res}')
# except ValueError:
#     print('Turi buti iveskas skaicius!')
#
# except ZeroDivisionError:
#     print('Dalyba is nulio negalima. Iveskite kita skaiciu')

#
# num = input("Iveskite skaiciu: ")
#
# try:
#     number = int(num)
#
# except ValueError:
#     print('Konvertacija nesekminga, bandykite dar karta')
#
# else:
#     print(f'Konversija sekminga {number}')
#
# finally:
#     print('Programa baige darba')

# Funkcija tikrins amziu
# def tikrinti_amziu(amzius):
#     if amzius < 0:
#         raise ValueError('Amzius negali buti neigiamas')
#     elif amzius >= 18:
#         print('Vartotojas pilnameits')
#     else:
#         print('Vartotojas nepilnametis')
# tikrinti_amziu(-5)
# tikrinti_amziu(15)
# tikrinti_amziu(21)

from datetime import datetime
print(datetime)
print(datetime.today)
# import datetime

dt_res = datetime.datetime.today()
print(dt_res)
print(dt_res.year)
print(dt_res.month)
for i in range(1, 1000000):
    a = 123
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(dt_res.microsecond)
print(f'End - {datetime.datetime.today()}')