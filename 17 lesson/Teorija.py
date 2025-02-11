from ipaddress import summarize_address_range

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self._atlyginimas = None
#         self._asmens_kodas = None
#
#     def get_atlyginimas(self):
#         if self._atlyginimas:
#             print(self._atlyginimas)
#         else:
#             print('Atlyginimas dar nepaskirtas')
#
#     def set_atlyginimas(self, suma):
#             if suma > 0:
#                 self._atlyginimas = suma
#             else:
#                 print('Atlyginimas negali buti < 0')
#
#     def get_asment_kodas(self):
#         if self._asmens_kodas:
#             print(self._asmens_kodas)
#         else:
#             print('Asmens kodas dar nepaskirtas.')
#
#     def set_asmens_kodas(self, asmnes_kodas):
#         if asmnes_kodas > 0:
#             self._asmens_kodas = asmnes_kodas
#         else:
#             print('Atliginimas negali buti  <=0')
#
#     def get_darbuotojas_info(self):
#             print(f'Vardas: {self.vardas}')
#             print(f'Pavarde: {self.pavarde}')
#             print(f'Pareigos: {self.pareigos}')
#             self.get_atlyginimas()
#             self.get_asment_kodas()
#
# class Vadovas(Darbuotojas):
#     def __init__(self, vardas, pavarde, pareigos, departamentas):
#         super().__init__(vardas, pavarde, pareigos)
#         self.departamentas = departamentas
#
#     def super_change_of_asmens_kodas(self):
#         self.__asmens_kodas = '123123123'
# darbuotojas1 = Darbuotojas('Jonas', 'Jonaitis', 'Programuotojas')
# darbuotojas1.set_atlyginimas('1000')
# darbuotojas1._atlyginimas = '123'
# darbuotojas1.get_darbuotojas_info()


class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None

    @property
    def atliginimas(self):
        return self.__atlyginimas if self.__atlyginimas else 0

    @atliginimas.setter
    def atliginimas(self, suma):
        self.__atlyginimas = suma if suma >= 0 else 1

darb1 = Darbuotojas('Jonas', 'Jonaitis', 'Direktorius')

atl = darb1.atliginimas
print(atl)
darb1.atliginimas = 5000

atl2 = darb1.atliginimas
print(atl2)


class Calculator:
    @staticmethod
    def