all_rooms = []


class Room(object):

    def __init__(self, room_type=None, capacity=None):
        self.room_type = room_type.strip().upper()
        self.capacity = capacity

    def create_room(self, *args):
        # Run validation before adding to storage structure.
        for room in args:
            if not room.isalpha():
                return 'Error.All rooms must be alphabetical in nature.'
            if len(room) == 0:
                return 'A blank space cannot be a new name.'
        try:
            for room in args:
                single_room = {}
                if self.room_type == 'L':
                    single_room['room_name'] = room.title()
                    single_room['room_capacity'] = self.capacity
                    single_room['room_type'] = self.room_type
                    single_room['occupants'] = []
                    all_rooms.append(single_room)
                elif self.room_type == 'O':
                    single_room['room_name'] = room.title()
                    single_room['room_capacity'] = self.capacity
                    single_room['room_type'] = self.room_type
                    single_room['occupants'] = []
                    all_rooms.append(single_room)
        except Exception:
            return 'An error occurred.'


class LivingSpace(Room):
    def __init__(self):
        super(LivingSpace, self).__init__(room_type='L', capacity=4)


class Office(Room):
    def __init__(self):
        super(Office, self).__init__(room_type='O', capacity=6)


living = LivingSpace()
living.create_room('python', 'ruby')
office = Office()
office.create_room('pton', 'Narnia')
print(all_rooms)
print(len(all_rooms))
