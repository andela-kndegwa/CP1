ALL_ROOMS = []
ROOMS = {
    'offices': [],
    'livingSpaces': []
}

offices = []
living_spaces = []


class Room(object):
    """
    This class models both the Living Space and Office
    space in the proposed Amity Room Allocation System.
    The Room class is a Super Class from which both
    Living Space Class and Office Class are Sub Classes of.
    Its main inheritable attrubute is
    Room name alias room_name
    """

    def __init__(self, room_type='', capacity=None):
        self.room_type = room_type
        self.capacity = capacity
        print('A')

    def create_room(self, args):
        '''
        This action is intended to create a room
        with its first argument defining the room type
        and then proceeds to add them to their respective
        list as either office or livingSpace.
        The initial checks are all validation checks
        '''
        print('B')
        # self.args = args
        if type(self.room_type) != str:
            return 'Room type must be a string.'
        if self.room_type not in ['O', 'L']:
            return 'Room type must be either O or L.'
        for room in args:
            print('for loop; room', room)
            if not str(room).isalpha():
                return 'Error. All room names must be alphabetical in nature.'
            try:

                print('C', room)
                if self.room_type == 'O':
                    print('room type is O')
                    single_room = {}
                    # offices.append(room.title())
                    single_room['room_name'] = room
                    single_room['room_type'] = self.room_type
                    single_room['room_capacity'] = self.capacity
                    single_room['occupants'] = []
                    ALL_ROOMS.append(single_room)
                    print(ALL_ROOMS)
                elif self.room_type == 'L':
                    print('room type is L')
                    living_spaces.append(room.title())
                    single_room['room_name'] = self.room_name
                    single_room['room_type'] = self.room_type
                    single_room['room_capacity'] = self.capacity
                    single_room['occupants'] = []
                    ALL_ROOMS.append(single_room)
                    print(ALL_ROOMS)
            except Exception as e:
                print(e)
                return 'An error occured.'
        print('D')
        return ALL_ROOMS


class OfficeSpace(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
    """

    def __init__(self, room_name, room_type='O', capacity=4):
        print('-A')
        Room.__init__(self, room_name, room_type)
        print('E')


class LivingSpace(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
    """

    def __init__(self, room_name, room_type='L', capacity=4):
        Room.__init__(self, room_name)


o = OfficeSpace('O')
print('initialized')
ret = o.create_room('Krypton', 'Oculus')
print(ret)
