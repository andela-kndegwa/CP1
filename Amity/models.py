import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Fellow(Base):
    __tablename__ = 'fellow'
    id = Column(Integer, primary_key=True)
    fellow_name = Column(String(250), nullable=False)


class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    staff_name = Column(String(250), nullable=False)


class LivingSpace(Base):
    __tablename__ = 'livingspace'
    id = Column(Integer, primary_key=True)
    ls_name = Column(String(250), nullable=False)
    wants_accomodation = Column(Boolean, unique=False, default=False)
    fellow_id = Column(Integer, ForeignKey('fellow.id'))
    fellow = relationship(Fellow)


class Office(Base):
    __tablename__ = 'office'
    id = Column(Integer, primary_key=True)
    of_name = Column(String(250), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    staff = relationship(Staff)
    fellow_id = Column(Integer, ForeignKey('fellow.id'))
    fellow = relationship(Fellow)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///test_amity.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
