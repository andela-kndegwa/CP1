room_names = []


class Room(object):
    """
    This class models both the Living Space and Office
    space in the proposed Amity Room Allocation System.
    The Room class is a Super Class from which both
    Living Space Class and Office Class are Sub Classes of.
    Inheritable attributes are:
    1. Room name alias room_name
    2. Room ID alias room_id
    """

    def __init__(self):
        pass

    def create_room(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = []
        if type(self.room_name) is str:
            room_names.append(self.room_name.title())

    def check_room_occupants(self):
        if len(self.occupants) == 0:
            return "There are no occupants in this room as yet."
        for occupant in self.occupants:
            return occupant + '\n'


class LivingSpace(Room):
    """
    The Living Space class is a sub-class of the 'Room'
    class meaning it inherits characteristics such as
    'room_name' and 'room_id'.
    """

    def __init__(self, room_name, room_type, room_capacity):
        Room.__init__(self, room_name, room_type)
        self.room_capacity = 4

    def check_occupants(self, room_name):
        if self.occupants >= self.room_capacity:
            return "Maxium Number Reached"


class Office(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits characteristics such as
    'room_name' and 'room_id'.
    """

    def __init__(self, room_name, room_type, room_capacity):
        Room.__init__(self, room_name, room_type)
        self.room_capacity = 6

    def check_occupants(self, room_name):
        if self.occupants >= self.room_capacity:
            return "Maxium Number Reached"

