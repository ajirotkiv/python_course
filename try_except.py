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


num = input("Iveskite skaiciu: ")

try:
    number = int(num)

except ValueError:
    print('Konvertacija nesekminga, bandykite dar karta')

else:
    print(f'Konversija sekminga {number}')

finally:
    print('Programa baige darba')