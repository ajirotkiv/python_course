import sqlite3

conn = sqlite3.connect('pavyzdys.db')
c = conn.cursor()
c.execute(
'''
CREATE TABLE IF NOT EXISTS studentai (
    vardas  TEXT,
    pavarde TEXT,   
    klase INTEGER)
'''
)

conn.commit()
conn.close()

def init_database():
    conn = sqlite3.connect('pavyzdys.db')
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS studentai (
            vardas  TEXT,
            pavarde TEXT,   
            klase INTEGER)
        '''
    )

    conn.commit()
    conn.close()

def append_to_studentai(vardas, pavarde, klase):
        with sqlite3.connect('pavyzdys.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)", (vardas, pavarde, klase))

def print_all_studentai_row():
        with sqlite3.connect('pavyzdys.db') as conn:
            c = conn.cursor()
            for row in c.execute("SELECT * FROM studentai"):
                print(row)
append_to_studentai('Jonas', 'Jonaitis', 11)
append_to_studentai('Tomas', 'Tomaitis', 11)
append_to_studentai('Marius', 'Martonas', 11)
append_to_studentai('Gitanas', 'Nauseda', 11)
append_to_studentai('Dalia', 'Gribauskaite', 11)
print_all_studentai_row()