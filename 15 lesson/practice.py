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