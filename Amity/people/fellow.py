from person import Person


class Fellow(Person):
    """
    The Fellow class is a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """
    def __init__(self):
        pass


f = Fellow()
f.add_person('Migwi', 'Ndungu', 'Fellow', 'Y')
print(f.people_stats)    
