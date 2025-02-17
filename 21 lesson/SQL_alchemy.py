from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'projektai'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    kaina = Column(Float)

Base.metadata.create_all(engine)

from models import Projektas, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

pavadinimas = input('Iveskite projekto pavadinima: ')
kaina = float(input('Iveskite kaina: '))

row_object = Projektas(pavadinimas=pavadinimas, kaina=kaina)
session.add(row_object)
session.commit()

all_rows = session.query(Projektas).all()

for row in all_rows:
    print(row)

for row in all_rows:
    print(f'ID: {row.id}, Pavadinimas: {row. pavadinimas}, Kaina: {row.kaina}')
