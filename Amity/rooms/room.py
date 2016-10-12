class Room(object):

    def __init__(self, room_type=None, capacity=None):
        self.room_type = room_type.strip().upper()
        self.capacity = capacity

    def get_cap(self):
        print 'Capacity is %s'%self.capacity


class LivingSpace(Room):
    def __init__(self):
        super(LivingSpace, self).__init__(room_type='L', capacity=4)


class Office(Room):
    def __init__(self):
        super(Office, self).__init__(room_type='O', capacity=6)

