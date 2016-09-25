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


class LivingSpace(Room):
    """
    The Living Space class is a sub-class of the 'Room'
    class meaning it inherits characteristics such as
    'room_name' and 'room_id'.
    """
    pass


class Office(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits characteristics such as
    'room_name' and 'room_id'.
    """
    pass
