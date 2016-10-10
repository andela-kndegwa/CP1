from random import randint

offices = []
living_spaces = []
rooms = {
    'offices': offices,
    'livingSpaces': living_spaces

}

staff = []
fellows = []

people = {
    'staff': staff,
    'fellows': fellows

}

people_stats = []

f_ids = [0]
s_ids = [0]


allocations = []


def create_room(room_type, *args):
    '''
    This action is intended to create a room
    with its first argument defining the room type
    and then proceeds to add them to their respective
    list as either office or livingSpace.
    The initial checks are all validation checks

    '''
    if type(room_type) != str:
        return 'Error. Enter O for office or L for living space.'
    room_type = room_type.strip()
    room_type = room_type.upper()
    for arg in args:
        if type(arg.strip()) != str:
            return 'Error. Room names must be words.'
    try:
        if room_type not in ['O', 'L']:
            return 'Invalid Room Type entered'
        for room in args:
            if room_type == 'O':
                offices.append(room.title())
            elif room_type == 'L':
                living_spaces.append(room.title())
    except Exception:
        return 'An error occurred in the command'


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
        return 'The user %s has been successfully added' % full_name
    except Exception:
        return 'Oops! An error occurred.'


def get_room_type(room):
    if type(room) != str:
        return 'Error! Please enter correct format for room as string.'
    room = room.title()
    if room in rooms['offices']:
        return '%s is an Office Space.' % room
    elif room in rooms['livingSpaces']:
        return '%s is a Living Space.' % room
    else:
        return 'The room does not exist in our system'


def allocate_room(person_id, room_type):
    # Validation checks
    # If type entered is not string return msg
    if type(person_id) != str and type(room_type) != str:
        msg = 'Please enter ID in the format '
        msg += '<person_type_initial><number> '
        msg += 'e.g S23 or F45.'
        msg += 'The room type must also either be O or L'
        return msg
    # if person_id starts with S return msg because
    # staff cannot be allocated living space
    if person_id.upper().startswith('S') and room_type.upper() == 'L':
        msg = 'A staff member cannot be allocated '
        msg += 'a living space. Enter F <number>'
        return msg
    single_allocation = {}
    # This dictionary holds a single allocation details
    # i.e person_id : living space allocated
    person_id = person_id.upper()
    room_type = room_type.upper()
    # Ensure offices and living spaces exist before assignment
    if room_type == 'O' and len(rooms['offices']) == 0:
        return 'No offices added. Please add an office before allocation. '
    elif room_type == 'L' and len(rooms['livingSpaces']) == 0:
        return 'No living spaces added. Please add a living space.'
    get_ids = []
    for person in people_stats:
        if person['person_id']:
            get_ids.append(person['person_id'])
    if person_id.upper() not in get_ids:
        return 'The fellow ID entered does not exist.'
    if person_id.startswith('S'):
        single_allocation[person_id] = offices[
            randint(0, (len(offices) - 1))]
        allocations.append(single_allocation)
    elif person_id.startswith('F'):
        for identifier in range(len(get_ids)):
            if people_stats[identifier]['person_id'] == person_id:
                if people_stats[identifier]['wants_accomodation'] == 'N':
                    return 'The fellow does not want accomodation.'
                else:
                    if room_type == 'L':
                        single_allocation[person_id] = living_spaces[
                            randint(0, (len(living_spaces) - 1))]
                        allocations.append(single_allocation)
                    elif room_type == 'O':
                        single_allocation[person_id] = offices[
                            randint(0, (len(offices) - 1))]
                        allocations.append(single_allocation)
    return allocations


def reallocate_room(person_id, room_type):
    # Validate then write code
    if type(person_id) != str:
        msg = 'Please enter ID in the format '
        msg += '<person_type_initial><number> '
        msg += 'e.g S23 or F45'
        return msg
    person_id = person_id.upper()
    room_type = room_type.upper()
    if bool(person_id.startswith('S')) is False and \
            bool(person_id.startswith('F')) is False:
        msg = 'Error. Please enter correct format as '
        msg += '<person_type><number> e.g S45 or F90.'
        return msg
    if room_type not in ['O', 'L']:
        return 'Error. Enter O for office space or L for living space'
    if person_id.startswith('S') and room_type == 'L':
        msg = 'A staff member cannot be allocated '
        msg += 'or reallocated a living space.'
        return msg
    for allocation in allocations:
        if allocation[person_id] and allocation[person_id]\
                in rooms['offices'] and room_type == 'O':
            msg = 'Person ID %s was formerly allocated ' % person_id
            msg += 'to the office %s. \n' % allocation[person_id]
            prev_room = allocation[person_id]
            allocation[person_id] = offices[randint(0, (len(offices) - 1))]
            new_room = allocation[person_id]
            while prev_room == new_room:
                allocation[person_id] = offices[randint(0, (len(offices) - 1))]
            msg += 'New office allocated is %s' % allocation[person_id]
            return msg
        elif allocation[person_id] and allocation[person_id] \
                in rooms['livingSpaces'] and room_type == 'L':
            msg = 'Person ID %s was formerly allocated ' % person_id
            msg += 'to the living space %s \n' % allocation[person_id]
            prev_room = allocation[person_id]
            allocation[person_id] = living_spaces[
                randint(0, (len(living_spaces) - 1))]
            new_room = allocation[person_id]
            while prev_room == new_room:
                allocation[person_id] = living_spaces[
                    randint(0, (len(living_spaces) - 1))]
            msg += 'New living space allocated is %s' % allocation[person_id]
            return msg
    return allocations
