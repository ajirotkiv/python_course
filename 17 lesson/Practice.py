# 1. Apsaugoti Atributai (Protected Attributes)
# Užduotis:
# Sukurkite klasę Studentas, kuri turi atributus vardas, pavarde ir apsaugotą atributą
# _pazymiai.
# • Pridėkite metodą prideti_pazymi(), kuris leidžia pridėti pažymį, jei jis yra tarp 1 ir
# 10.
# • Sukurkite metodą rodyti_vidurki(), kuris apskaičiuoja pažymių vidurkį.
# from io import valid_seek_flags


class Studentas:
    def __init__(self, vardas, pavarde, _pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []
        self.vidurkis = None

    def prideti_pazymi(self, pazymis: int):
        if pazymis > 1 and pazymis < 10:
            self._pazymiai.append(pazymis)
        else:
            print('Pazymis turi buti tarp 1 iki 10')

    def rodyti_vidurki(self):
        if self._pazymiai:
            self.vidurkis = round(sum(self._pazymiai) / len(self._pazymiai))
            print(f'Studento {self.vardas} {self.pavarde} pazymiu vidurkis yra: {self.vidurkis}')
        else:
            print('Pazymiu nera')

studentas1 = Studentas('Jonas', 'Jonaitis', 6)
studentas2 = Studentas('Tomas', 'Tomaitis', 9)
studentas1.prideti_pazymi(5)
studentas2.prideti_pazymi(8)
studentas1.prideti_pazymi(2)
studentas2.prideti_pazymi(4)
studentas1.prideti_pazymi(8)
studentas2.prideti_pazymi(7)
studentas1.rodyti_vidurki()
studentas2.rodyti_vidurki()


# Papildoma užduotis:
# Paveldėkite klasę Studentas ir sukurkite klasę StudentasLyderis, kuri papildomai gali
# pridėti „bonus“ taškų prie vidurkio.
#
# class StudentasLyderis(Studentas):
#     def __init__(self, vardas, pavarde, pazymiai, bonus_taskai):
#         super().__init__(vardas, pavarde, pazymiai)
#         self.bonus_taskai = bonus_taskai
#         self.studentai = []
#
#     def prideti_bonus_taskus(self, lideris):
#         for lideris in self.studentai:
#             lyderis = max(self.studentai, key=lambda name:
#                           sum(self.studentai[name]) / len(self.studentai[name]))
#             geriausias_vidurkis = sum(self.studentai[lideris] / len(self.studentai[lyderis]))
#             bonus_taskai = 10
#             vidurkis_bonus = geriausias_vidurkis + bonus_taskai
#             return vidurkis_bonus
#         print(f'Lideris yra: {lideris}')
#
#
#
# 3. @property Dekoratorius
# Užduotis:
# Sukurkite klasę Darbuotojas, kuri turi atributus vardas, pavarde ir privatų atributą
# __atlyginimas.
# • Naudokite @property dekoratorių, kad galėtumėte gauti ir nustatyti atlyginimą.
# • Užtikrinkite, kad atlyginimas negali būti mažesnis nei minimalus (pvz., 500).
# Papildoma užduotis:
# Pridėkite papildomą @property metodą mokesciai, kuris apskaičiuoja mokesčius (pvz.,
# 20% nuo atlyginimo).

# class Darbuotojas:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.__atlyginimas = None
#         self.minimum = 500
#
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas
#
#     @atlyginimas.setter
#     def atliginimas(self, suma):
#         self.__atlyginimas = suma if suma >= 0 else 1
#
# darb1 = Darbuotojas('Jonas', 'Jonaitis')
#
# atl = darb1.atlyginimas
# print(atl)
# darb1.atlyginimas = 5000
# print(atl)
class Darbuotojas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = None
        self.
    @property
    def atliginimas(self):
        return self.__atlyginimas if self.__atlyginimas else 0

    @atliginimas.setter
    def atliginimas(self, suma):
        min = 500
        self.__atlyginimas = suma if suma >= min else 0

darb1 = Darbuotojas('Jonas', 'Jonaitis')

atl = darb1.atliginimas
darb1.atliginimas = 5000
print(atl)
darb1.atliginimas = 300

