import sqlite3

with sqlite3.connect('mokiniai.db') as conn:
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mokiniai (
            vardas TEXT,
            pavarde TEXT,
            klase INT,
            vidurkis INT
            )
        ''')

with sqlite3.connect('mokytojai.db') as conn:
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mokytojai (
            vardas TEXT,
            pavarde TEXT,
            dalykas TEXT
            )
        ''')
class Asmuo:
    def __init__(self, id, vardas, pavarde):
        self.id = id
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, id, vardas, pavarde, klase, vidurkis):
        super().__init__(id, vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis
        self.indeksas = 0

    with sqlite3.connect('mokiniai.db') as conn:
        c = conn.cursor()
    def __iter__(self):
        return iter([self.id, self.vardas, self.pavarde, self.klase, self.vidurkis])

    def __next__(self):
        if self.indeksas < len(self.id):
            mokinys = self.id[self.indeksas]
            self.indeksas += 1  # Pereiname prie kito mokinio
            return mokinys
        else:
            # Jei mokiniai baigėsi, keliamas StopIteration išimtis, kad pabaigtume iteraciją
            raise StopIteration


mokinys1 = Mokinys(1, 'Jonas', 'Jonaitis', 10, 6)
mokinys2 = Mokinys(1, 'Tomas', 'Tomaitis', 10, 8)
mokinys3 = Mokinys(1, 'Marius', 'Mariukas', 11, 5)
for savybe in mokinys1:
    print(savybe)

class Mokytojas(Asmuo):
    def __init__(self, id, vardas, pavarde, dalykas):
        super().__init__(id, vardas, pavarde)
        self.dalykas = dalykas

def prideti_mokini(id, vardas, pavarde, klase, vidurkis):
    with sqlite3.connect('mokiniai.db') as conn:
        c = conn.cursor()
        c.execute('EXECUTE INTO mokiniai(id, vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)', (id, vardas, pavarde, klase, vidurkis))

def prideti_mokytoja(id, vardas, pavarde, dalykas):
    with sqlite3.connect('mokytojai.db') as conn:
        c = conn.cursor()
        c.execute('EXECUTE INTO mokytojai(vardas, pavarde, dalykas) VALUES (?, ?, ?, ?)', (id, vardas, pavarde, dalykas))

def atnaujinti_mokini(id, naujas_vidurkis):
    conn = sqlite3.connect('mokiniai.db')
    c = conn.cursor()
    c.execute('UPDATE mokiniai SET vidurkis = ? WHERE id = ?', (id, naujas_vidurkis))

def atnaujinti_mokytoja(id, naujas_dalykas):
    conn = sqlite3.connect('mokytojai.db')
    c = conn.cursor()
    c.execute('UPDATE mokytojai SET dalykas = ? WHERE id = ?', (id, naujas_dalykas))

def istrinti_mokini(id, vardas, pavarde, klase):
    conn = sqlite3.connect('mokiniai.db')
    c = conn.cursor()
    c.execute('DELETE FROM mokiniai WHERE id = ? WHERE vardas = ? WHERE pavarde = ? WHERE klase = ?', (id, vardas, pavarde, klase))

def istrinti_mokytoja(id, vardas, pavarde, dalykas):
    conn = sqlite3.connect('mokytojai.db')
    c = conn.cursor()
    c.execute('DELETE FROM mokytojai WHERE id = ? WHERE vardas = ? WHERE pavarde = ? WHERE dalykas = ?', (id, vardas, pavarde, dalykas))

def mokiniu_paieska():
    with sqlite3.connect('mokiniai.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokiniai"):
            print(row)

def mokytoju_paieska():
    with sqlite3.connect('mokytojai.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokiniai"):
            print(row)

class MokiniuIteratorius:
    def __init__(self, mokiniai):
        self.mokiniai = mokiniai
        self.indeksas = 0

    def __iter__(self):
        return iter(self.mokiniai)

    def __next__(self, id, vardas, pavarde, klase, vidurkis):
        # Patikriname, ar yra dar mokinių

        if self.indeksas < len(self.mokiniai):
            mokinys = self.mokiniai[self.indeksas]
            self.indeksas += 1  # Pereiname prie kito mokinio
            return mokinys
        else:
            raise StopIteration

# Sukuriame iteratorių su mokiniais
iteratorius = MokiniuIteratorius(mokinys)

# Naudojame iteratorių for cikle
for mokinys in iteratorius:
    print(f"Vardas: {mokinys['vardas']}, Pavardė: {mokinys['pavarde']}, Amžius: {mokinys['amzius']}")


conn.commit()
conn.close()