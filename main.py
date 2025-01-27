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
user = ''
def trys_sveikinimai(vardas1, vardas2, vardas3):
    greetings = f'Labas, {vardas1}', f'Labas, {vardas2}', f'Labas, {vardas3}'
    return greetings
res = trys_sveikinimai('Adomas', 'Petras', 'Jurate')
print(res)


# Užduotis 4:
# Sukurkite funkciją sveikink_su_pavadinimu(vardas, pavadinimas="drauge"), kuri
# atspausdintų žinutę: „Sveikas, [vardas]! Ką veiki, [pavadinimas]?“.
# 1. Iškvieskite funkciją nenurodydami pavadinimo.
# 2. Iškvieskite funkciją, nurodydami pavadinimą „kolega“.

def sveikink_su_pavadinimu(vardas, pavadinimas="drauge"):
    print(f'Sveikas, {vardas}! Ka veiki, {pavadinimas}?')
sveikink_su_pavadinimu('Bernotas')
sveikink_su_pavadinimu('Lukas', 'kaimine')