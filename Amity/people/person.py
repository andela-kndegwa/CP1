fellows = []
staff = []

people = {
    'fellows': fellows,
    'staff': staff

}

people_stats = []

f_ids = [0]
s_ids = [0]


class Person(object):
    def __init__(self, person_type=None):
        self.person_type = person_type

    def get_person_type(self):
        return 'Person type is %s' % self.person_type

    # def add_person(self, name, person_type, wants_accomodation='N'):
    #     """b
    #     This function adds a person and proceeds the respective
    #     instance and appends them to a list.
    #     """
    #     full_name = name.split(" ")
    #     if not (full_name[0].isalpha() or full_name[1].isalpha()):
    #         return 'All your words must be alphabetical in nature.'
    #     # Check person type
    #     if self.person_type not in ['Fellow', 'Staff']:
    #         return 'Please enter Fellow or Staff for person type.'
    #     # Check wants_accomodation to be either Y or N
    #     if wants_accomodation not in ['Y', 'N']:
    #         return 'Please enter Y or N for accomodation.'
    #     if self.person_type == 'Staff' and wants_accomodation == 'Y':
    #         return 'A Staff member cannot be allocated accomodation.'


class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(person_type='Staff')


class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(person_type='Fellow')


s = Staff()
print(s.get_person_type())