from sqlalchemy import *
from models import DataBaseManager

db = DataBaseManager()


def remove_similar_db_existence(db_name):
    '''
    This method removes the amity.sqlite db if it already exists
    '''
    if os.path.exists(db_name):
        os.remove(db_name)


def get_people_from_db():
    pass


def add_people_to_db():
    pass


def add_rooms_to_db():
    pass


def remove_person_from_db():
    pass
