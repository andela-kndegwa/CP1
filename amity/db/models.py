from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    person_identifer = Column(String(250), unique=True, nullable=False)
    person_name = Column(String(250), nullable=False)
    person_type = Column(String(250), nullable=False)
    wants_accomodation = Column(Boolean, default=False)
    office_allocated = Column(String(250), nullable=False)
    living_space_allocated = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Person(person_name='%s')>" % self.person_name


class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)
    room_capacity = Column(Integer)

    def __repr__(self):
        return "<Room(room_name='%s')>" % self.room_name


class DatabaseManager(object):
    """
    Creates a db connection object
    """

    def __init__(self):
        self.db_name = 'default_amity_db.sqlite'
        self.engine = create_engine('sqlite:///' + self.db_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
