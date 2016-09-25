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
    pass


class Fellow(Person):
    """
    The Fellow class is a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """
    pass


class Staff(Person):
    """
    The Staff class is also a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """
    pass
