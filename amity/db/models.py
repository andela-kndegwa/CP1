from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    person_identifier = Column(String(250), unique=True)
    person_name = Column(String(250))
    person_type = Column(String(250))
    wants_accomodation = Column(String(25))
    office_allocated = Column(String(250))
    living_space_allocated = Column(String(250))

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

    def __init__(self, db_name):
        self.db_name = db_name
        self.engine = create_engine('sqlite:///' + self.db_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)


db = DatabaseManager('amity.db')