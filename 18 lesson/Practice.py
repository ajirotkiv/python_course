# 4. @staticmethod Dekoratorius
# Užduotis:
# Sukurkite klasę Matematika, kuri turi statinius metodus:
# • sudeti(a, b) – grąžina dviejų skaičių sumą.
# • atimti(a, b) – grąžina dviejų skaičių skirtumą.
# • dauginti(a, b) – grąžina sandaugą.
# • dalinti(a, b) – grąžina dalmenį, bet įsitikinkite, kad nedalinama iš nulio.
# Papildoma užduotis:
# Pridėkite statinį metodą ar_lyginis(skaicius), kuris patikrina, ar skaičius yra lyginis.

# class Matematika:
#     @staticmethod
#     def sudeti(a, b):
#         return a + b
#     @staticmethod
#     def atimti(a, b):
#         return a - b
#     @staticmethod
#     def dauginti(a, b):
#         return a * b
#     @staticmethod
#     def dalinti(a, b):
#         if b == 0:
#             return a / b
#     @staticmethod
#     def ar_lyginis(skaicius):
#         return skaicius % 2 ==0
#     skaicius = int(input('Iveskite skaiciu: '))
#     if ar_lyginis(skaicius):
#         print('Skaicius yra lyginis')
#     else:
#         print('Skacius yra nelyginis')


# 5. @classmethod Dekoratorius
# Užduotis:
# Sukurkite klasę Automobilis, kuri turi atributus marke, modelis, metai.
# • Pridėkite klasės metodą sukurti_is_string(), kuris sukuria objektą iš teksto
# eilutės, pvz.: "Toyota Corolla 2020".
# Papildoma užduotis:
# Pridėkite klasės metodą naujausias_modelis(), kuris grąžina naujausią automobilį iš
# pateikto automobilių sąrašo.

# class Automobilis:
#     def __init__(self, marke, modelis, metai):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = int(metai)
#     @classmethod
#     def sukurti_is_string(cls, eilute):
#         marke, modelis, metai = eilute.split()
#         return cls(marke, modelis, metai)
#     @classmethod
#     def naujausias_modelis(cls, Automobilis):
#         return max(Automobilis, key=lambda
#             auto: auto.metai)
#     def __str__(self):
#         return f'{self.marke} {self.modelis} {self.metai}'
#
# auto1 = Automobilis('Toyota', 'Corolla', 2003),
# auto2 = Automobilis('BMW', 'X6', 2011),
# auto3 = Automobilis('Audi', 'A4', 2000)
# Automobilis.naujausias_modelis()


# print('Naujausias automobilis: ', naujausias_automobilis)

# 1. Funkcijos kaip Pirmos Klasės Objektai
# Užduotis:
# Sukurkite šias funkcijas:
# 1. prideti_zenkliuka(tekstas) – prideda žvaigždutę * prie teksto pabaigos.
# 2. apversti_teksta(tekstas) – apverčia pateiktą tekstą.
# 3. Sukurkite funkciją apdoroti_teksta(tekstas, funkcija=None), kuri:
# a. Jei nurodyta funkcija, pritaiko ją tekstui.
# b. Jei funkcija nenurodyta, tiesiog grąžina tekstą mažosiomis raidėmis.
# Papildoma užduotis:
# Sukurkite funkciją keli_apdorojimai(tekstas, *funkcijos), kuri pritaiko kelias
# funkcijas iš eilės tam pačiam tekstui.
# def prideti_zenkliuka(tekstas):
#     return tekstas + "*"
#
# def apversti_teksta(tekstas):
#     return tekstas[::-1]
# def apdoroti_teskta(tekstas, funkcija = None):
#     if funkcija:
#         tekstas = funkcija(tekstas)
#     else:
#         return tekstas.upper()
# def keli_apdorojimai(tekstas, *funkcijos):
#     return tekstas(*funkcijos)
#
# print(apversti_teksta('sashmatai'))
# print(apdoroti_teskta('Blablabla', apversti_teksta(tekstas=))

# 2. Dekoratoriai
# Užduotis:
# Sukurkite dekoratorių sekimo_dekoratorius, kuris:
# 1. Išveda žinutę prieš ir po funkcijos vykdymo:
# a. Prieš: „Vykdoma funkcija: <funkcijos_pavadinimas>“
# b. Po: „Funkcija baigta!“
# 2. Pridėkite dekoratorių prie funkcijos dauginti(a, b), kuri grąžina dviejų skaičių
# sandaugą.
# Papildoma užduotis:
# Pridėkite funkciją dalinti(a, b) su tuo pačiu dekoratoriumi. Jei b == 0, grąžinkite
# klaidos pranešimą.

def sekimo_dekoratorius(funkcija):
    def wrapper(*args, **kwargs):
        # Prieš vykdymą
        print(f"Vykdoma funkcija: {funkcija.__name__}")

        # Funkcijos vykdymas
        rezultatas = funkcija(*args, **kwargs)

        # Po vykdymo
        print("Funkcija baigta!")

        return rezultatas

    return wrapper


# Naudojame dekoratorių funkcijoms

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b


@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return "Klaida: negalima dalyti iš 0"
    return a / b


# Pavyzdžiai
print(dauginti(5, 3))
print(dalinti(10, 0))
print(dalinti(10, 2))
