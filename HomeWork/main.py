# 1. Sudėtinė užduotis
# Užduotis:
# Sukurkite bazinę klasę Zmogus, su atributais vardas, pavarde ir metodu
# prisistatyti(), kuris spausdina žmogaus vardą ir pavardę.
# Sukurkite paveldinčią klasę Studentas, kuri perrašo prisistatyti() metodą,
# pridėdama informaciją apie studijų programą.
# Sukurkite klasę Universitetas, kuri naudoja kompoziciją, turėdama sąrašą
# Studentas objektų.
# Pridėkite metodus prideti_studenta() ir rodyti_visus_studentus().
# Papildoma užduotis:
# Sukurkite kelis Studentas objektus.
# Pridėkite juos į Universitetas objektą.
# Parodykite visų studentų informaciją, pasitelkiant paveldėjimą, metodų perrašymą
# ir kompoziciją.

class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def prisistatyti(self):
        return f'Vardas: {self.vardas}, pavardė: {self.pavarde}'

class Studentas(Zmogus):
    def __init__(self, vardas, pavarde, studiju_programa):
        super().__init__(vardas, pavarde)
        self.studiju_programa = studiju_programa

    def prisistatyti(self):
        super().prisistatyti()
        print(f'Studento vardas: {self.vardas}, pavarde: {self.pavarde}, studiju programa: {self.studiju_programa}')

# mokinys = Studentas('Mantas', 'Matukas', 'programavimas')
# mokinys.prisistatyti()


class Universitetas():
    def __init__(self):
        self.students = []

    def prideti_studenta(self, mokinys):
        self.students.append(mokinys)

    def rodyti_visus_studentus(self):
        for mokinys in self.students:
            print(mokinys.prisistatyti())
while True:
    print('1. Prideti nauja studenta')
    print('2. Parodyti visus studentus')
    try:
        user_input = int(input('Pasirinkite veiksma: '))
        if user_input < 1 or user_input > 2:
            raise ValueError
    except ValueError:
        print('Iveskite 1 arba 2')
        continue
    if user_input == 1:
        try:
            vardas = input('Iveskite studento varda: ')
            pavarde = input('Iveskite studento pavarde: ')
            studiju_programa = input('Iveskite studiju programa: ')
            new_student = Studentas(vardas, pavarde, studiju_programa)
            Universitetas.prideti_studenta(new_student)
            print()
        except ValueError:
            print('Iveskite visus duomenys!')
    elif user_input == 2:
        Universitetas.rodyti_visus_studentus()

mokinys1 = Studentas('Mantas', 'Matukas', 'programavimas')
mokinys2 = Studentas('Jonas', 'Jonaitis', 'WEB dizainas')
mokinys3 = Studentas('Laima', 'Lape', 'SEO')

university = Universitetas()
university.prideti_studenta(mokinys1)
university.prideti_studenta(mokinys2)
university.prideti_studenta(mokinys3)
university.rodyti_visus_studentus()

