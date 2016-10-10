staff = []
fellows = []

people = {
    'staff': staff,
    'fellows': fellows

}

people_stats = []

f_ids = [0]
s_ids = [0]


def add_person(first_name, last_name, person_type, wants_accomodation='N'):
    # Preceding validation checks.
    if type(first_name) != str or type(last_name) != str:
        # validates type input.
        return 'Invalid Name type passed'
    # Preformatting input for better storage in the structures
    first_name = first_name.strip()
    first_name = first_name.title()
    last_name = last_name .strip()
    last_name = last_name.title()
    person_type = person_type.strip()
    person_type = person_type.title()

    if person_type.title() not in ['Fellow', 'Staff']:
        # Fellow | Staff.
        return 'Invalid Person Type entered.'

    if wants_accomodation.upper() not in ['Y', 'N']:
        return 'Please enter either Y for Yes or N for No.'
        # Y -- > Yes or N --> No.

    if person_type == 'Staff' and wants_accomodation == 'Y':
        return 'A staff cannot be allocated a living space.'

    person_stats = {}
    # Person stats holds the specific person details to
    # be appended to a list --> people_stats
    # people_stats is a list of dictionaries for each person_stats

    person_stats['full_name'] = first_name + ' ' + last_name
    person_stats['person_type'] = person_type.title()
    person_stats['wants_accomodation'] = wants_accomodation.upper()
    full_name = first_name + ' ' + last_name

    '''
    After assigining person_stats['person_type'], we
    now proceed to figure out their id.
    '''
    try:
        if bool(people_stats) is False:
            if person_stats['person_type'] == 'Fellow':
                f_id = 1
                f_ids.append(f_id)
                person_stats['person_id'] = 'F' + str(f_id)
            elif person_stats['person_type' == 'Staff']:
                s_id = 1
                s_ids.append(s_id)
                person_stats['person_id'] = 'S' + str(s_id)
        else:
            '''
            Check first if person exists.
            '''
            full_name = first_name + ' ' + last_name
            for person in people_stats:
                if full_name == person['full_name']:
                    return 'Already exists!'
            if person_stats['person_type'] == 'Fellow':
                f_id = f_ids.pop() + 1
                person_stats['person_id'] = 'F' + str(f_id)
                f_ids.append(f_id)
            elif person_stats['person_type'] == 'Staff':
                s_id = s_ids.pop() + 1
                person_stats['person_id'] = 'S' + str(s_id)
                s_ids.append(s_id)
        people_stats.append(person_stats)
        if person_type.title() == 'Fellow':
            fellows.append(full_name)
            people['fellows'].append(full_name)
        elif person_type.title() == 'Staff':
            staff.append(full_name)
            people['staff'].append(full_name)
        return people_stats
    except Exception:
        return 'Oops! An error occurred.'
