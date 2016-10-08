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
    if person_type.upper() not in ['F', 'S']:
        return 'Invalid Person Type entered.'
    person_stats = {}
    # Person stats holds the specific person details to
    # be appended to a list --> people_stats
    person_stats['full_name'] = first_name + ' ' + last_name
    person_stats['person_type'] = person_type.upper()
    '''
    After assigining person_stats['person_type'], we
    now proceed to figure out their id.
    '''
    try:
        if bool(people_stats) is False:
            if person_stats['person_type'] == 'F':
                f_id = 1
                f_ids.append(f_id)
                person_stats['person_id'] = 'F' + str(f_id)
            elif person_stats['person_type' == 'S']:
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
            if person_stats['person_type'] == 'F':
                f_id = f_ids.pop() + 1
                person_stats['person_id'] = 'F' + str(f_id)
                f_ids.append(f_id)
            elif person_stats['person_type'] == 'S':
                s_id = s_ids.pop() + 1
                person_stats['person_id'] = 'S' + str(s_id)
                s_ids.append(s_id)
        people_stats.append(person_stats)
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


def allocate_living_space(person_id):
    single_allocation = {}
    person_ids = []
    for person in people_stats:
        if person['person_id'] and person['person_type'] == 'F':
            #Only a fellow can have a living space
            #A fellow and staff can receive a 
            person_ids.append(person['person_id'])
    if person_id.upper() not in person_ids:
        return 'The  Person ID you entered does not exist  or is not a fellow.'
    #randint(,0 len(offices))
    single_allocation[person_id.upper()] = living_spaces[randint(0, (len(living_spaces)-1))]
    #Random room allocation functionality for living space.
    allocations.append(single_allocation)
    return single_allocation






def reallocate_room(person_id, room_type):
    pass


#create_room('l', 'Modor', 'Valhalla', 'Oculus', 'Orange','Westside', 'Downtown')
#add_person('Kimani', 'Ndegwa', 'F')
#add_person('Hanna', 'Masila', 'F')
#add_person('Ha', 'Ma', 's')
#add_person('jaja', 'eving', 's')
#add_person('sads', 'ev', 's')
#print(allocate_living_space('f2'))
#print(people_stats)
#print(len(people_stats))

create_room('O', 'Narnia', 'Oculus', 'Whatever')
print(living_spaces)
add_person('Whitney', 'Ruoroh', 'f')
add_person('KImani', 'Ndegwa', 'f')
add_person('KIm', 'SOMEM', 's')
print(people_stats)