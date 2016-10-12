from rooms.room import LivingSpace, Office


class Amity(object):
    def __init__(self):
        self.all_rooms = []
        self.offices = []
        self.living_spaces = []
        self.rooms = {
            'offices': self.offices,
            'living_spaces': self.living_spaces
        }

    def create_room(self, room_type, room_name):
        if type(room_type) != str or room_type.upper() not in ['O', 'L']:
            return 'Please enter O or L for a room'
        single_room = {}
        if room_type.upper() == 'O':
            office = Office()
            single_room['room_name'] = room_name
            single_room['room_type'] = office.room_type
            single_room['room_capacity'] = office.capacity
            single_room['occupants'] = []
            self.offices.append(room_name)
        elif room_type.upper() == 'L':
            living = LivingSpace()
            single_room['room_name'] = room_name
            single_room['room_type'] = living.room_type
            single_room['room_capacity'] = living.capacity
            single_room['occupants'] = []
            self.living_spaces.append(room_name)
        self.all_rooms.append(single_room)
        return 'The room %s has been created.' % room_name
