class Asmuo:
    def __init__(self, vardas, pavarde, gim_metai):
        self.vardas = vardas
        self. pavarde = pavarde
        self.gim_metai = gim_metai

class MokinioTevas(Asmuo):
    def __init__(self, vardas, pavarde, gim_metai, darbuoviete):
        super().__init__(vardas, pavarde, gim_metai)
        self.darbuoviete = darbuoviete
tevas = MokinioTevas(1, 2, 3, 4)

print(tevas.vardas)
print(tevas.darbuoviete)


class Mygtukas:
    def deaktyvuoti(self):
        print('Mygtukas deaktyvuotas')

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print('Spalva pasikeite i rausva')

red_bnt = RaudonasMygtukas()
red_bnt.deaktyvuoti()