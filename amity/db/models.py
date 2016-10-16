from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    person_identifer = Column(String(250), unique=True, nullable=False)
    person_name = Column(String(250), nullable=False)
    person_type = Column(String(250), nullable=False)
    wants_accomodation = Column(Boolean, default=False)

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


# class Fellow(Base):
#     __tablename__ = 'fellow'
#     id = Column(Integer, primary_key=True)
#     fellow_name = Column(String(250), nullable=False)
#     created_date = Column(DateTime, default=datetime.datetime.utcnow)
#     wants_accomodation = Column(Boolean, default=True)

#     def __repr__(self):
#         return "<Fellow(fellow_name='%s')>" % self.fellow_name


# class Staff(Base):
#     __tablename__ = 'staff'
#     id = Column(Integer, primary_key=True)
#     staff_name = Column(String(250), nullable=False)
#     created_date = Column(DateTime, default=datetime.datetime.utcnow)

#     def __repr__(self):
#         return "<Staff(staff_name='%s')>" % self.staff_name


# class LivingSpace(Base):
#     __tablename__ = 'livingspace'
#     id = Column(Integer, primary_key=True)
#     ls_name = Column(String(250), nullable=False)
#     wants_accomodation = Column(Boolean, unique=False, default=False)
#     fellow_id = Column(Integer, ForeignKey('fellow.id'))
#     fellow = relationship(Fellow)

#     def __repr__(self):
#         return "<Living Space(ls_name='%s')>" % self.ls_name


# class Office(Base):
#     __tablename__ = 'office'
#     id = Column(Integer, primary_key=True)
#     of_name = Column(String(250), nullable=False)
#     created_date = Column(DateTime, default=datetime.datetime.utcnow)
#     staff_id = Column(Integer, ForeignKey('staff.id'))
#     staff = relationship(Staff)
#     fellow_id = Column(Integer, ForeignKey('fellow.id'))
#     fellow = relationship(Fellow)

#     def __repr__(self):
#         return "<Office(office_name='%s')>" % self.office_name


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
