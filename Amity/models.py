import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Fellow(Base):
    __tablename__ = 'fellow'
    id = Column(Integer, primary_key=True)
    fellow_name = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Fellow(fellow_name='%s')>" % self.fellow_name


class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    staff_name = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Staff(staff_name='%s')>" % self.staff_name


class LivingSpace(Base):
    __tablename__ = 'livingspace'
    id = Column(Integer, primary_key=True)
    ls_name = Column(String(250), nullable=False)
    wants_accomodation = Column(Boolean, unique=False, default=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    fellow_id = Column(Integer, ForeignKey('fellow.id'))
    fellow = relationship(Fellow)

    def __repr__(self):
        return "<Living Space(ls_name='%s')>" % self.ls_name


class Office(Base):
    __tablename__ = 'office'
    id = Column(Integer, primary_key=True)
    of_name = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    staff = relationship(Staff)
    fellow_id = Column(Integer, ForeignKey('fellow.id'))
    fellow = relationship(Fellow)

    def __repr__(self):
        return "<Office(office_name='%s')>" % self.office_name


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///test_amity.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
