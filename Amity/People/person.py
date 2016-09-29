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

    def create_person(self, person_name, person_type, wants_accomodation):
        self.person_name = person_name
        self.person_type = person_type
        self.wants_accomodation = wants_accomodation
