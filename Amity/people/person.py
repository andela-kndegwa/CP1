class Person(object):
    def __init__(self, person_type=None):
        self.person_type = person_type

    def get_person_type(self):
        return 'Person type is %s' % self.person_type



class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(person_type='Staff')


class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(person_type='Fellow')


