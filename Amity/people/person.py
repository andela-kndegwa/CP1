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
        self.staff = []
        self.fellows = []
        self.people = {
            'staff': self.staff,
            'fellows': self.fellows

        }
        self.people_stats = []

        self.f_ids = [0]
        self.s_ids = [0]

    def add_person(self, first_name, last_name, person_type, wants_accomodation='N'):
        # Preceding validation checks.
        if type(self.first_name) != str or type(self.last_name) != str:
            # validates type input.
            return 'Invalid Name type passed'
        # Preformatting input for better storage in the structures
        self.first_name = first_name.strip()
        self.first_name = first_name.title()
        self.last_name = last_name .strip()
        self.last_name = last_name.title()
        self.person_type = person_type.strip()
        self.person_type = person_type.title()

        if self.first_name.isalpha() is False or self.last_name.isalpha() is False:
            msg = 'Please ensure '
            msg += 'both your first name and second name'
            msg += 'are alphabetical in nature.'
            return msg

        if self.person_type.title() not in ['Fellow', 'Staff']:
            # Fellow | Staff.
            return 'Invalid Person Type entered.'

        if self.wants_accomodation.upper() not in ['Y', 'N']:
            return 'Please enter either Y for Yes or N for No.'
            # Y -- > Yes or N --> No.

        if self.person_type == 'Staff' and self.wants_accomodation == 'Y':
            return 'A staff cannot be allocated a living space.'

        person_stats = {}
        # Person stats holds the specific person details to
        # be appended to a list --> people_stats
        # people_stats is a list of dictionaries for each person_stats
        full_name = self.first_name + ' ' + self.last_name
        person_stats['full_name'] = full_name
        person_stats['person_type'] = self.person_type
        person_stats['wants_accomodation'] = self.wants_accomodation.upper()
        '''
        After assigining person_stats['person_type'], we
        now proceed to figure out their id.
        '''
        try:
            if bool(self.people_stats) is False:
                if self.person_stats['person_type'] == 'Fellow':
                    self.f_id = 1
                    selff_ids.append(f_id)
                    person_stats['person_id'] = 'F' + str(f_id)
                elif person_stats['person_type'] == 'Staff':
                    s_id = 1
                    s_ids.append(s_id)
                    person_stats['person_id'] = 'S' + str(s_id)
            else:
                '''
                Check first if person exists.
                '''
                if person_stats['person_type'] == 'Fellow':
                    f_id = f_ids.pop() + 1
                    person_stats['person_id'] = 'F' + str(f_id)
                    f_ids.append(f_id)
                elif person_stats['person_type'] == 'Staff':
                    s_id = s_ids.pop() + 1
                    person_stats['person_id'] = 'S' + str(s_id)
                    s_ids.append(s_id)
            people_stats.append(person_stats)
            if person_type == 'Fellow':
            fellows.append(full_name)
        elif person_type == 'Staff':
            staff.append(full_name)
        return people_stats
    except Exception:
        return 'Oops! An error occurred.'

p = Person()
p.add_person('KImani', 'Ndegwa', 'Fellow', 'y')
print(p.people_stats)
