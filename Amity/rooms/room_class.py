ALL_ROOMS = []
ROOMS = {
    'offices': [],
    'livingSpaces': []
}


class Room(object):

    def __init__(self, room_type, *args):
    	room_names = args
        self.room_type = room_type
        if self.room_type == "O":
            self.capacity = 6
            

        elif self.room_type == "L":
            self.capacity = 4

    def create_room(self, room_type, *args):
        if room_type not in ["O", "L"]:
            return "Invalid Room Type!"
        else:
            if room_type == "O":
                for room in args:
                    single_allocation = {}
                    single_allocation['room_name'] = room
                    single_allocation['room_type'] = room_type
                    single_allocation['room_capacity'] = self.capacity
                    single_allocation['occupants'] = []
                    print(single_allocation)
                    # ROOMS['offices'].append(room)
                    # ALL_ROOMS.append(single_allocation)
        # return ALL_ROOMS

