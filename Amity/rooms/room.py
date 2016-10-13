class Room(object):

    def __init__(self, room_name, room_type=None, capacity=None):
        self.room_type = room_type.strip().title()
        self.capacity = capacity
        self.room_name = room_name.title()
        self.occupants = []

    def add_person(self, person):
        self.occupants.append(person)
        self.capacity = self.capacity - 1
        return 'Person added.'


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(
            room_name, room_type='Living Space', capacity=4)


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type='Office', capacity=6)


ls = LivingSpace('Valhalla')
print(ls.occupants)
