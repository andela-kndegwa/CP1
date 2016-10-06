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


def create_room(room_type, *args):
    '''
    This action is intended to create a room
    with its first argument defining the room type
    and then proceeds to add them to their respective
    list as either office or livingSpace

    '''
    try:
        if room_type.upper() not in ['O', 'L']:
            return 'Invalid Room Type entered'
        for room in args:
            if room_type.upper() == 'O':
                offices.append(room)
            elif room_type.upper() == 'L':
                living_spaces.append(room)
    except Exception:
        return 'An error occurred in the command'


def add_person(first_name, last_name, person_type):
    if type(first_name) != str or type(last_name) != str:
        return 'Invalid Name type passed'
    if person_type not in ['F', 'S']:
        return 'Invalid Person Type entered.'
    try:
        full_name = first_name + ' ' + last_name
        if person_type.upper() == 'F':
            fellows.append(full_name)
            people['fellows'].append(full_name)
        elif person_type.upper() == 'S':
            staff.append(full_name)
            people['staff'].append(full_name)
        return 'The user %s has been successfully added' % full_name
    except Exception:
        return 'Error'


def get_room_type(room):
    if room in rooms['offices']:
        return 'Is Office'
    elif room in rooms['livingSpaces']:
        return 'Is Living Space'
    else:
        return 'The room does not exist in our system'


def allocate_room(person_id, room_name):
    pass


def reallocate_room(person_id, room_type):
    pass
