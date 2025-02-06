# 2. Paveldėjimas (Inheritance)
# Užduotis:
# Sukurkite bazinę klasę Gyvunas, kuri turi atributus vardas ir amzius.
# Pridėkite metodą judeti(), kuris spausdina, kad gyvūnas juda.
# Sukurkite dvi paveldinčias klases: Kate ir Suo.
# Kate klasėje pridėkite metodą miaukseti(), kuris sako "Vardas sako MIAU!"
# Suo klasėje pridėkite metodą lot(), kuris sako "Vardas sako AU AU!"
# Papildoma užduotis:
# Sukurkite Kate ir Suo objektus, iškvieskite jų metodus ir patikrinkite, ar paveldėjimas
# veikia.

class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f'{self.vardas} juda :-)')

class Kate(Gyvunas):
    def miaukseti(self):
        print(f'{self.vardas} sako MIAU!!!')

class Suo(Gyvunas):
    def lot(self):
        print(f'{self.vardas} sako AU AU')

cat = Kate('Uma', 12)
cat.miaukseti()
cat. judeti()

dog = Suo('Leo', 8)
dog.lot()
dog.judeti()


print('-------------')
# 3. Komponavimas (Composition)
# Užduotis:
# Sukurkite klasę Variklis, kuri turi atributą galia ir metodą startuoti(), kuris
# spausdina "Variklis veikia su galia: X arklio galių".
# Tada sukurkite klasę Automobilis, kuri turi atributus marke ir modelis, bei naudoja
# Variklis kaip savo atributą.
# • Pridėkite metodą vaziuoti(), kuris iškviečia startuoti() metodą.
# Papildoma užduotis:
# Sukurkite kelis Automobilis objektus su skirtingais varikliais ir priverskite juos važiuoti.
from symtable import Class

class Variklis:
    def __init__(self, galia):
        self.galia = galia

    def startuoti(self):
        print(f'Variklis veikia su galia {self.galia} arklio galiu')

class Automobilis(Variklis):
    def __init__(self, marke, modelis, galia):
        self.marke = marke
        self.modelis = modelis
        self.galia = galia

    def vaziuoti(self):
        print(f'{self.marke} {self.modelis} vaziuoja!!!')
        Variklis.startuoti(self)

car1 = Automobilis('Toyota', 'RAV4', '180')
car2 = Automobilis('Nissan', 'Telega', '200')
car1.vaziuoti()
car2.vaziuoti()
print('-------------')
# 4. Konstruktoriaus Perrašymas
# Užduotis:
# Sukurkite tėvinę klasę Asmuo, kuri turi atributus vardas ir amzius.
# • Sukurkite konstruktorių, kuris nustato šiuos atributus.
# Sukurkite paveldinčią klasę Darbuotojas, kuri paveldi Asmuo ir prideda papildomą
# atributą pareigos.
# • Perrašykite konstruktorių naudodami super(), kad pridėtumėte pareigos.
# Papildoma užduotis:
# Sukurkite Darbuotojas objektą ir atspausdinkite visą informaciją apie jį

class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos

darbuotojas1 = Darbuotojas('Jonas', 30, 'programuotojas')
darbuotojas2 = Darbuotojas('Petras', 50, 'vairuotojas')

print(f'Darbuotojo vardas: {darbuotojas1.vardas}, amzius:{darbuotojas1.amzius}, pareigos: {darbuotojas1.pareigos}')

print('-------------')

# 5. Kitų Metodų Perrašymas (Overriding)
# Užduotis:
# Sukurkite klasę TransportoPriemone su metodu judeti(), kuris spausdina „Transporto
# priemonė juda“.
# Sukurkite paveldinčią klasę Dviratis, kuri perrašo judeti() metodą, kad spausdintų
# „Dviratis važiuoja pedalais“.
# Papildoma užduotis:
# Sukurkite TransportoPriemone ir Dviratis objektus bei patikrinkite jų judeti()
# metodų veikimą.

class TransportoPriemone:
    def judeti(self):
        print('Transporto priemonė juda')

class Dviratis(TransportoPriemone):
    def judeti(self):
        super().judeti()
        print('Dviratis vaziuoja pedalais')

bike = Dviratis()
bike.judeti()

