class Kijana(object):
    def __init__(self):
        self.offices = []
        self.living_spaces = []

    def create_room(self, rm, rt):
        self.rm = rm
        self.rt = rt
        if self.rt.upper() not in ['O', 'L']:
            return 'Invalid Room Type'
        if self.rm and self.rt:
            if self.rt.upper() == 'O':
                self.offices.append(self.rm)
            elif self.rt.upper() == 'L':
                self.living_spaces.append(self.rm)
        return 'Error'


a = Kijana()
a.create_room('Valhalla', 'o')
print(a.living_spaces)
