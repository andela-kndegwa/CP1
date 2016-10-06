from office import OfficeSpace
from living_space import LivingSpace


class Room(object):
    """
    This class models both the Living Space and Office
    space in the proposed Amity Room Allocation System.
    The Room class is a Super Class from which both
    Living Space Class and Office Class are Sub Classes of.
    Its main inheritable attrubute is
    Room name alias room_name
    """
    mapper = {
        'O': 'Office',
        'L': 'Living Space'
    }

    def __init__(self):
        self.room_name = ''
        self.room_type = ''
        self.occupants = []
        self.offices = []
        self.living_spaces = []

    def create_room(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        if self.room_type not in ['O', 'L']:
            return 'INVALID ROOM TYPE.'
        try:
            if self.room_type.upper() == 'O':
                o = OfficeSpace()
                self.offices.append(o)
                return self.offices
            elif self.room_type.upper() == 'L':
                living = LivingSpace()
                self.living_spaces.append(living)

                self.offices.append(room_name)
                return self.offices
            elif self.room_type.upper() == 'L':
                self.living_spaces.append(room_name)
                return self.living_spaces
            else:
                return "Invalid Command Parsed"
        except Exception:
            return 'An error occurred creating the room!'

    def check_room_occupants(self):
        if len(self.occupants) == 0:
            return "There are no occupants in this room as yet."
        else:
            return len(self.occupants)

