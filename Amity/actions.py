from Rooms.office import OfficeSpace
from Rooms.living_space import LivingSpace


class Amity(object):
    '''
    This class is the main class as per the UML diagrams
    drawn in the /designs folder. It models the whole Amity
    system and seeks to bring all the functions and attributes
    into one central place.
    '''

    def __init__(self):
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.allocated_rooms = []
        self.unallocated_rooms = []
        self.available_rooms = []
        self.unavailable_rooms = []
        self.staff = []
        self.fellows = []

    def create_room(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        try:
            if self.room_name and self.room_type:
                if self.room_name in self.rooms:
                    return 'Room name already exists.'
                if len(self.room_name) > 1:
                    for room in self.room_name:
                        if self.room_type is 'O':
                            room = OfficeSpace()
                            self.offices.append(room)
                            msg = 'The office(s) have been successfully added'
                        elif self.room_type is 'L':
                            room = LivingSpace()
                            self.living_spaces.append(room)
                            msg = 'The living spaces(s) have been successfully added'
                else:
                    return 'msg'
        except Exception:
            msg = 'An error occurred running your command.'
        return msg


a = Amity()
print(a.offices)
a.create_room(['Valhalla', 'Oculus'], 'O')
print (a.offices)