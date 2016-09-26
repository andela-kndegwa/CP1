class Room(object):
    """
    This class models both the Living Space and Office
    space in the proposed Amity Room Allocation System.
    The Room class is a Super Class from which both
    Living Space Class and Office Class are Sub Classes of.
    Its main inheritable attrubute is
    Room name alias room_name
    """

    def __init__(self):
        pass

    def create_room(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = []

    def check_room_occupants(self):
        if len(self.occupants) == 0:
            return "There are no occupants in this room as yet."
        else:
            for occupant in self.occupants:
                return occupant + '\n'



class LivingSpace(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
    """
    room_capacity = 4


class Office(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
    """
    room_capacity = 6
