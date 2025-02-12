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

conn.commit()
conn.close()