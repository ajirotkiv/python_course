# 4. Generatoriai
# Užduotis:
# Sukurkite generatorių fib_generator(n), kuris grąžina pirmus n Fibonacci skaičius.
# • Fibonacci seka: 0, 1, 1, 2, 3, 5, 8, 13, …
# Papildoma užduotis:
# Sukurkite generatorių filtruoti_lyginius(seka), kuris iš pateiktos skaičių sekos
# grąžina tik lyginius skaičius.

# Fibonacci sekos generatorius
# def fib_generator(n):
#     a, b = 0, 1  # Pradinis Fibonacci sekos elementas
#     for i in range(n):
#         yield a  # Grąžina dabartinį Fibonacci skaičių
#         a, b = b, a + b  # Pereina prie kito skaičiaus
#
# # Generatorius, filtruojantis tik lyginius skaičius
# def filtruoti_lyginius(seka):
#     for skaicius in seka:
#         if skaicius % 2 == 0:  # Patikrina, ar skaičius yra lyginis
#             yield skaicius
#
# # Pavyzdys, kaip naudoti generatorius
# n = 30  # Pavyzdžiui, norime pirmų 10 Fibonacci skaičių
#
# # Sukuriame Fibonacci sekos generatorių
# fibonacci_sk = fib_generator(n)
#
# # Filtruojame tik lyginius Fibonacci skaičius
# lyginiu_fibonacci_sk = filtruoti_lyginius(fibonacci_sk)
#
# # Spausdiname lyginius Fibonacci skaičius
# print(f"Pirmi {n} Fibonacci skaičiai (tik lyginiai):")
# for skaicius in lyginiu_fibonacci_sk:
#     print(skaicius)

# 1. Prisijungimas prie Duomenų Bazės
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Prisijungia prie SQLite duomenų bazės pavadinimu mokykla.db.
# b. Sukuria lentelę mokykla su stulpeliais: pavadinimas (TEXT), adresas
# (TEXT), mokiniu_skaicius (INTEGER).

import sqlite3

conn = sqlite3.connect('mokykla.db')
c = conn.cursor()
c.execute(
'''
CREATE TABLE IF NOT EXISTS mokykla (
    pavadinimas TEXT,
    adresas TEXT,   
    mokiniu_skaicius INTEGER)
'''
)

# conn.commit()
# conn.close()

# 2. Duomenų Įterpimas (INSERT)
# Užduotis:
# 1. Įterpkite šiuos duomenis į lentelę mokykla:
# a. "Vilniaus progimnazija", "Vilniaus g. 10", 500
# b. "Kauno gimnazija", "Kauno g. 5", 800
# 2. Parašykite Python funkciją prideti_mokykla, kuri priima tris parametrus
# (pavadinimas, adresas, mokinių skaičius) ir įterpia juos į duomenų bazę.

def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)", (pavadinimas, adresas, mokiniu_skaicius))

prideti_mokykla('Vilniaus progimnazija', 'Vilniaus g. 10', 500)
prideti_mokykla('Kauno gimnazija', 'Kauno g. 5', 800)


# 3. Duomenų Skaitymas (SELECT)
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Nuskaito visus duomenis iš lentelės mokykla.
# b. Išveda juos tvarkingai formatuotu tekstu (pvz., „Mokykla: Vilniaus
# progimnazija, Adresas: Vilniaus g. 10, Mokinių skaičius: 500“).
# 2. Pridėkite galimybę filtruoti duomenis pagal minimalų mokinių skaičių (pvz., rodyti
# tik tas mokyklas, kuriose yra daugiau nei 600 mokinių)

def print_all_mokykla_row():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokykla"):
            print(row)




# 4. Duomenų Atnaujinimas (UPDATE)
# Užduotis:
# 1. Parašykite Python funkciją atnaujinti_mokiniu_skaiciu, kuri:
# a. Priima mokyklos pavadinimą ir naują mokinių skaičių kaip parametrus.
# b. Atnaujina nurodytos mokyklos mokinių skaičių duomenų bazėje.
# 2. Patikrinkite, ar atnaujinimas įvyko sėkmingai, išvesdami visų mokyklų sąrašą po
# pakeitimo.

def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute('UPDATE mokykla SET mokiniu_skaicius = ? WHERE pavadinimas = ?', (pavadinimas, naujas_skaicius))

atnaujinti_mokiniu_skaiciu('Kauno gimnazija', 400)


# print(print_all_mokykla_row())

# Uždarykite ryšį su duomenų baze
c.close()
conn.close()
