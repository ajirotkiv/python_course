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

# Pridėti mokinį
mokinys1 = Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=8)
session.add(mokinys1)
mokinys2 = Mokinys(vardas="Tomas", pavarde="Tomaitis", klase=9)
session.add(mokinys2)
mokinys3 = Mokinys(vardas="Jurga", pavarde="Jurgaite", klase=7)
session.add(mokinys3)

# Pridėti mokytoją
mokytojas1 = Mokytojas(vardas="Alfonsas", pavarde="Alfonsaitis", dalykas="Geografija")
session.add(mokytojas1)
mokytojas2 = Mokytojas(vardas="Zofija", pavarde="Zofiene", dalykas="Istorija")
session.add(mokytojas2)

# Patvirtinti pakeitimus ir įrašyti į duomenų bazę
session.commit()

visi_mokiniai = session.query(Mokinys).all()
for mokinys in visi_mokiniai:
    print (f"<Mokinys(id={mokinys.id}, vardas='{mokinys.vardas}', pavarde='{mokinys.pavarde}', klase={mokinys.klase})>")


visi_mokytojai = session.query(Mokytojas).all()
for mokytojas in visi_mokytojai:
    print (f"<Mokytojas(id={mokytojas.id}, vardas='{mokytojas.vardas}', pavarde='{mokytojas.pavarde}', klase={mokytojas.dalykas})>")