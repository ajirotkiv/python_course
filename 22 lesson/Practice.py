from sqlalchemy import func

# 1. Duomenų bazės ir modelio sukūrimas
# Užduotis:
# • Sukurkite SQLite duomenų bazę mokykla.db.
# • Sukurkite SQLAlchemy modelį Mokinys, kuris turės šiuos laukus:
# o id (pirminis raktas, Integer)
# o vardas (String)
# o pavarde (String)
# o klase (Integer)
# Papildomas iššūkis: Sukurkite antrą modelį Mokytojas, kuris turės laukus:
# • id (pirminis raktas, Integer)
# • vardas (String)
# • pavarde (String)
# • dalykas (String)

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

Base.metadata.create_all(engine)

# 2. Duomenų įterpimas
# Užduotis:
# • Įterpkite bent 3 mokinius ir 2 mokytojus į duomenų bazę naudojant SQLAlchemy
# ORM.
# • Užtikrinkite, kad duomenys būtų išsaugoti naudojant session.commit().
#  Papildomas iššūkis: Įterpkite naują mokinį tik tuo atveju, jei jo dar nėra duomenų
# bazėje.
# 3. Duomenų skaitymas
# Užduotis:
# • Parašykite funkciją, kuri išveda visų mokinių sąrašą.
# • Parašykite funkciją, kuri išveda visus mokytojus.

Session = sessionmaker(bind=engine)
session = Session()

# # Pridėti mokinį
# mokinys1 = Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=12)
# session.add(mokinys1)
# mokinys2 = Mokinys(vardas="Tomas", pavarde="Tomaitis", klase=12)
# session.add(mokinys2)
# mokinys3 = Mokinys(vardas="Jurga", pavarde="Jurgaite", klase=12)
# session.add(mokinys3)
#
# # Pridėti mokytoją
# mokytojas1 = Mokytojas(vardas="Alfonsas", pavarde="Alfonsaitis", dalykas="Geografija")
# session.add(mokytojas1)
# mokytojas2 = Mokytojas(vardas="Zofija", pavarde="Zofiene", dalykas="Istorija")
# session.add(mokytojas2)
#
# # Patvirtinti pakeitimus ir įrašyti į duomenų bazę
# session.commit()


# Funkcija, kuri tikrina, ar mokinys jau yra duomenų bazėje pagal vardą, pavardę, klase
def patikra_mokinys(vardas, pavarde, klase):
    return session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde, klase=klase).first() is not None

# # Įterpiame mokinius tik tuo atveju, jei jų dar nėra
# def patikra_mokinys(vardas, pavarde, klase):
#     mokiniai = session.query(Mokinys).all()
#
#     session.add(mokinys1)
#     print(mokinys1)
# visi_mokiniai = session.query(Mokinys).all()
# for mokinys in visi_mokiniai:
#     print (f"<Mokinys(id={mokinys.id}, vardas='{mokinys.vardas}', pavarde='{mokinys.pavarde}', klase={mokinys.klase})>")
#
#
# visi_mokytojai = session.query(Mokytojas).all()
# for mokytojas in visi_mokytojai:
#     print (f"<Mokytojas(id={mokytojas.id}, vardas='{mokytojas.vardas}', pavarde='{mokytojas.pavarde}', dalykas={mokytojas.dalykas})>")
#
# session.commit()

# 5. Duomenų trynimas
# Užduotis:
# • Parašykite funkciją, kuri pašalina mokinį iš duomenų bazės pagal id.
# • Parašykite funkciją, kuri pašalina mokytoją pagal id.
#  Papildomas iššūkis:
# • Ištrinkite visus mokinius, kurie jau baigė mokyklą (12 klasė).
#
# mokinys_id = 5
# mokinys_object = session.get(Mokinys, mokinys_id)
# print('Rastas mokinys: ', mokinys_object)
#
# session.delete(mokinys_object)
# session.commit()
#
# all_rows = session.query(Mokinys).all()
#
# mokytojas_id = 5
# mokytojas_object = session.get(Mokytojas, mokinys_id)
# print('Rastas mokytojas: ', mokytojas_object)
#
# session.delete(mokytojas_object)
# session.commit()

# filtered_mokinys = session.query(Mokinys). filter_by(klase=12).all()
# print(f'Mokiniai, kurie baige mokykla: {filtered_mokinys}')

# 6. Paieška ir filtravimas
# Užduotis:
# • Parašykite funkciją, kuri randa mokinį pagal vardą.
# • Parašykite funkciją, kuri randa visus mokinius, kurių pavardė prasideda raide "P".
#  Papildomas iššūkis:
# • Raskite visus mokytojus, kurių vardas baigiasi raide „s“.

# paieskos_pavadinimas = 'Jonas'
# filtered_mokinys_vardas = session.query(Mokinys).filter_by(vardas=paieskos_pavadinimas, klase=12).all()
# print(f'Surasti mokiniai pagal varda Jonas: {filtered_mokinys_vardas}')
#
# try:
#     filtered_mokinys_pavarde = session.query(Mokinys).filter_by(pavarde='P').first()
# except NoResultFound:
#     print('Nerasta tokia pavarde')
# except MultipleResultsFound:
#     print('Rastas daugiau negu vienas mokinys su tokia pavarde')
#
# print(filtered_mokinys_pavarde)

# Funkcija, kuri randa mokinį pagal vardą
# def rasti_mokini_pagal_varda(vardas):
#     mokinys = session.query(Mokinys).filter(Mokinys.vardas == vardas).first()
#     if mokinys:
#         print(f"Radome mokinį: {mokinys}")
#     else:
#         print(f"Mokinys su vardu '{vardas}' nerastas.")
#
# # Funkcija, kuri randa visus mokinius, kurių pavardė prasideda raide "P"
# def rasti_mokinius_pagal_pavarde_p(self):
#     mokiniai = session.query(Mokinys).filter(Mokinys.pavarde.like('P%')).all()
#     if mokiniai:
#         print("Mokiniai, kurių pavardė prasideda raide 'P':")
#         for mokinys in mokiniai:
#             print(mokinys)
#     else:
#         print("Mokinių su pavarde, prasidedančia raide 'P', nerasta.")
#
#
#
# # Funkcija, kuri randa visus mokytojus, kurių vardas baigiasi raide "s"
# def rasti_mokytojus_pagal_varda(mokinys):
#     mokytojai = session.query(Mokytojas).filter(Mokytojas.vardas.like('%s')).all()
#     if mokytojai:
#         print("Mokytojai, kurių vardas baigiasi raide 's':")
#         for mokytojas in mokytojai:
#             print(mokytojas)
#     else:
#         print("Mokytojų, kurių vardas baigiasi raide 's', nerasta.")
#
# # Pavyzdinis naudojimas
# rasti_mokini_pagal_varda('Jonas')
# rasti_mokinius_pagal_pavarde_p('Mok')




# 7. Rikiavimas ir skaičiavimai
# Užduotis:
# • Parašykite funkciją, kuri išveda visus mokinius pagal klasę (didėjančia tvarka).
# • Parašykite funkciją, kuri suskaičiuoja, kiek yra mokinukų kiekvienoje klasėje.
#  Papildomas iššūkis:
# • Suskaičiuokite vidutinį mokinių skaičių klasėje.

def mokiniu_rikiavimas_pagal_klase():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    for mokinys in mokiniai:
        print((mokinys.pavarde, mokinys.klase))
mokiniu_rikiavimas_pagal_klase()

def mokiniu_skaicius_klaseje():
    viso_mokiniu_klaseje = session.query(func.sum(Mokinys.klase)).scalar()
    print(f'Viso mokiniu klaseje: {viso_mokiniu_klaseje}')

mokiniu_skaicius_klaseje()

from sqlalchemy import func


# Funkcija, kuri skaičiuoja vidutinį mokinių skaičių klasėje
def vidutinis_mokiniu_skaicius_klaseje():
    # Suskaičiuoti mokinių skaičių kiekvienoje klasėje
    klase_skaičius = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()

    if klase_skaičius:
        # Suskaičiuojame bendrą mokinių skaičių ir klasių skaičių
        bendras_mokiniu_skaicius = sum([sk[1] for sk in klase_skaičius])  # Susumuoja mokinius visose klasėse
        bendras_klasių_skaicius = len(klase_skaičius)  # Skaičiuoja klasių skaičių

        # Vidutinė klasėje esančių mokinių skaičius
        vidutiniskiekyb = bendras_mokiniu_skaicius / bendras_klasių_skaicius

        print(f"Vidutinis mokinių skaičius klasėje: {vidutiniskiekyb:.2f}")
    else:
        print("Nėra mokinių duomenų.")


# Pavyzdinis funkcijos iškvietimas
vidutinis_mokiniu_skaicius_klaseje()
