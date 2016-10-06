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
        self.room_name = ''
        self.room_type = ''
        self.occupants = []
        self.offices = []
        self.living_spaces = []


