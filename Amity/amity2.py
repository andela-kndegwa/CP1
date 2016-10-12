class Amity(object):

    def create_room(self, room_type, *args):
        if room_type == 'L':
            ls = LivingSpace()
            rooms = ls.create_room(args)
        elif room_type == 'O':
            office = Office()
            rooms = office.create_room(args)
        return rooms

    def add_person():
        pass
    """
    For the docopt funcionality we will have the
    """


a = Amity()
x = a.create_room('L', 'Krypton', 'Oculus', 'Marble')
print(x)
