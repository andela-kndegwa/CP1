from Amity.rooms.room import Room, LivingSpace, OfficeSpace


class Amity(object):
    def __init__(self):
        pass

    def create_room(self, room_type, *args):
        '''
        This action is intended to create a room
        with its first argument defining the room type
        and then proceeds to add them to their respective
        list as either office or livingSpace.
        The initial checks are all validation checks
        '''
        # self.room_type = raw_input('Enter Room Type:\n')
        if not room_type.isalpha():
            return 'Error. Room type must be alphabet'
        if room_type not in ['O', 'L']:
            return 'Enter O or L for a room type.'
        if room_type == 'L':
            livingspace = LivingSpace()
            livingspace.create_room(args)
        elif room_type == 'O':
            office = OfficeSpace()
            office.create_room(args)

a = Amity()
a.create_room("O", "Room One", "Room Two")
print(Room.all_rooms)
