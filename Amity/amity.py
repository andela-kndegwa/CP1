import os
import sys
from models import Fellow, Staff, Office, LivingSpace
from database import session
from Rooms.living_space import LivingSpace
from Rooms.office import Office
from People.fellow import Fellow
from People.staff import Staff


class Amity(object):
    def __init__(self):
        pass

    def create_room(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        if self.room_type is 'O':
            office = Office.create_room(room_name)
            session.add(office)
            session.commit()
