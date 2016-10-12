ALL_ROOMS = []
ROOMS = {
    'offices': [],
    'livingSpaces': []
}


class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name


class Office(Room):

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.create_room(self.room_name)

    def create_room(self, *args):
        for room in args:
            ROOMS["offices"].append(room)


class LivingSpace(Room):

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.create_room(self.room_name)

    def create_room(self, *args):
        for room in args:
            ROOMS["livingSpaces"].append(room)


def create_room(room_type, *args):
    if room_type == "O":
        for room in args:
        	office = Office(room)
    elif room_type == "L":
    	for room in args:
    		livingspace = LivingSpace(room)

print(ROOMS)