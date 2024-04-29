from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firtname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firtname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return('{} {} {} {} {}'.format(self.ssn, self.firstname, self.lastname, self.gender, self.age))
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12355, "Mike", "john", "m", 35)
session.add(person)
session.commit()

result = session.query(Person).all()
print(result)
    