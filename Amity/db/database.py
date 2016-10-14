from sqlalchemy import create_engine
from models import People, Rooms, Base, DatabaseManager


db = DatabaseManager()


def specify_path(new_path):
    db.db_name = new_path
    db.engine = create_engine('sqlite:///' + new_path)
    db.session.configure(bind=db.engine)
    Base.metadata.create_all(db.engine)


Base.metadata.bind = db.engine
s = db.session()


def add_people(people):
    """
    Takes the People's list and iterates to add to db
    """

    try:
        for person in people:

            person_to_db = People(
                person_identifier=person.identifier,
                person_name=person.full_name,
                person_type=person.person_type
            )
            s.merge(person_to_db)

        s.commit()
        s.close()
        message = "People added to '{}' database successfully".\
            format(db.db_name)
        return message
    except Exception:
        return "Error encountered when adding people to db"


def add_rooms(rooms):
    """
    Takes a dictionary of room details and adds them to the database
    """

    for room in rooms:

        room_to_db = Rooms(
            room_name=room.room_name,
            room_capacity=room.room_capacity,
            room_type=room.room_type,
        )
        s.merge(room_to_db)

        s.commit()

    s.close()
    message = "Rooms added to '{}' database successfully".\
        format(db.db_name)
    return message
