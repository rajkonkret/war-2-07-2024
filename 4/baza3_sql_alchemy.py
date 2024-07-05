# ORM - Mapowanie obiektowo-relacyjne (ang. Object Relational Maping - ORM)
# sqlalchemy - sytem orm do współpracy z baza
# pip install sqlalchemy

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# echo=True właczenie logowania polecen bazy danych
# engine = create_engine('sqlite:///:memory:', echo=True)  # baza w pamięci
engine = create_engine('sqlite:///moja_baza_danych.db', echo=True)  # baza w pliku
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addressses = relationship('Address',
                              back_populates='person',
                              order_by='Address.email',
                              cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addressses')

    def __str__(self):
        return self.email

    __repr__ = __str__


# encje - klasy odwzorowywujace tabele w bazie danych
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi Wan Kenobi", age=45)
obi.addressses = [
    Address(email='obi@example.com'),
    Address(email='waaka@example.com'),
]

obi2 = Person(name='obi', age=54)
session.add(anakin)
session.add(obi)
session.add(obi2)
session.commit()

all_ = session.query(Person).all()
print(all_)  # [Anakin (id=1), Obi Wan Kenobi (id=2)]

an1 = session.query(Person).first()
print(an1)
obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()
print(obi_list)
# [Obi Wan Kenobi (id=2), obi (id=3)]
for o in obi_list:
    print(f"id: {o.id}, name: {o.name}")
# id: 2, name: Obi Wan Kenobi
# id: 3, name: obi
