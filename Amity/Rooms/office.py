from room import Room


class OfficeSpace(Room):
    """
    The Office class is also a sub-class of the 'Room'
    class meaning it inherits 'room_name'.
        """
    roomCapacity = 6
    occupants = []

    def get_all_occupants(self):
        pass

