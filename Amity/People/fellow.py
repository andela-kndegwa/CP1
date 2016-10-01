from person import Person


class Fellow(Person):
    """
    The Fellow class is a sub-class of the 'Person'
    class meaning it inherits characteristics such as
    'name' and 'p_id'.
    """

    def get_office_allocated(self):
        pass

    def get_living_space_allocated(self):
        pass

    def check_wants_accomodation(self):
        if self.wants_accomodation.upper() == 'Y':
            return 'Wants accomodation'
        elif self.wants_accomodation.upper() == 'N':
            return 'Declines accomodaion'
        else:
            return 'Last response invalid'
    