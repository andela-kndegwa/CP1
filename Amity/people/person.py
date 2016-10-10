from people_actions import add_person


class Person(object):
    """
    This class models both the fellows and staff
    in the proposed Amity Room Allocation System.
    The Person class is a Super Class from which both
    Fellow Class and Staff Class are Sub Classes of.
    The fellows and staff members have two common
    things that this Class defines i.e:
    1. Name denoted as 'name'
    2. Personal Identifier denoted as 'p_id'
    """

    def __init__(self):
        pass

    def add_person(self, first_name, last_name,
                   person_type, wants_accomodation='N'):
        self.people_stats = add_person(first_name, last_name,
                                       person_type, wants_accomodation='N')
        return self.people_stats


p = Person()
p.add_person('KImani', 'Ndegwa', 'Fellow', 'y')
x = p.add_person('Brian', 'Wan', 'Fellow')
print(x)
