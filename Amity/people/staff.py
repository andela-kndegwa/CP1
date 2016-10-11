from person import Person


class Staff(Person):
    """
    The Staff class is also a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """
    def __init__(self):
        pass


s = Staff()
s.add_person('Samuel', 'Gaamuwa', 'Staff')


