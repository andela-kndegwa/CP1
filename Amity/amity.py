import time
import click
from random import randint
from rooms.room import LivingSpace, Office
from people.person import Fellow, Staff


class Amity(object):
    '''
    Amity is the main class that uses the imported
    inherited classes:
    1.LivingSpace, Office ---> Room
    2.Staff, Fellow ---> Person
    This class instantiates the above sub classes and
    appropriately performs operations from them.
    '''

    def __init__(self):
        self.rooms = []
        self.offices = {
            'available': [],
            'unavailable': []
        }
        self.living_spaces = {
            'available': [],
            'unavailable': []
        }
        self.fellows = []
        self.staff = []
        self.people = self.staff + self.fellows
        # self.rooms = {
        #     'offices': self.offices,
        #     'living_spaces': self.living_spaces
        # }
        # # Regarding People
        # self.fellows = []
        # self.staff = []
        # self.people = {
        #     'fellows': self.fellows,
        #     'staff': self.staff
        # }
        # self.people_stats = []
        # # f_ids and s_ids is used to generate the IDS
        # # fellows ID Example ---> F23
        # # staff ID example ---> S15
        self.f_ids = [0]
        self.s_ids = [0]
        # # Regarding allocations
        self.staff_allocations = []
        self.fellow_allocations = []
        # self.office_details = {
        #     'available': [],
        #     'unavailable': []
        # }
        # self.ls_details = {
        #     'available': [],
        #     'unavailable': []
        # }

    def create_room(self, room_type, room_name):
        '''
        The create_room method in the amity class takes
        in room_type and room_name and instantiates those rooms.
        An office is created as an instance of the Office class.
        A living space is created as an instance of the LivingSpace class.
        -->The single room dictionary holds information regarding
        a specific single room and appends this to the rooms
        list
        '''
        if type(room_type) != str or room_type.upper() not in ['O', 'L']:
            click.secho('Error.Please enter O or L for a room type.',
                        bold=True, fg='red')
            return 'Error. Invalid room type initial.'
        room_type = room_type.strip().title()
        room_name = room_name.strip().title()
        if room_type.upper() == 'O':
            room = Office(room_name)
            self.offices['available'].append(room.room_name)
        elif room_type.upper() == 'L':
            room = LivingSpace(room_name)
            self.living_spaces['available'].append(room.room_name)
        self.rooms.append(room)
        click.secho('The %s ---> %s has been created.' %
                    (room.room_type, room.room_name), bold=True, fg='green')
        return 'Room %s created.' % room.room_name

    def print_allocations(self):
        """
        This prints allocations to the screen and
        highlights if they are empty or have any
        occupants, thereafter printing everyone who
        is in the particular room.
        """
        if not self.rooms:
            click.secho('THERE ARE NO ROOMS IN THE SYSTEM.',
                        fg='red', bold=True)
            return 'Error. No rooms within system.'
        for room in self.rooms:
            click.secho(room.room_name, fg='cyan')
            click.secho('==' * 10, fg='cyan')
            if room.occupants:
                for occupant in room.occupants:
                    click.secho(occupant)
            else:
                click.secho(
                    'There are no people in this room yet.', fg='cyan')

    def add_person(self, first_name, other_name, person_type,
                   accomodate='N'):
        if type(first_name) != str or type(other_name) != str:
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        if first_name.isalpha() is False or other_name.isalpha() is False:
            click.secho('Person names need be alphabetical in nature',
                        fg='red', bold=True)
            return 'Non-Alphanumeric names added'
        if person_type.title() not in ['Fellow', 'Staff']:
            person_type = person_type.title()
            click.secho('Please enter either Fellow or Staff for person type',
                        fg='red', bold=True)
            return 'Invalid Person Type'
        if accomodate.upper() not in ['Y', 'N']:
            click.secho('Please enter Y or N for wants accomodation.',
                        fg='red', bold=True)
            return 'Wants accomodation not Y or N'
        if person_type == 'Staff' and accomodate == 'Y':
            click.secho(
                'A Staff member cannot be allocated accomodation.', fg='red', bold=True)
            return 'Staff cannot have wants allocation of Yes.'
        if accomodate.upper() == 'Y' and person_type == 'Fellow':
            if not self.living_spaces['available']:
                click.secho(
                    'Please add a living space for a fellow to be allocated both room types.')
                return 'No Living space for fellow requiring both.'
            if not self.offices['available']:
                click.secho(
                    'Please add an office for a fellow to be allocated both room types.')
                return 'No office for fellow requiring both.'
        if not self.rooms:
            msg = 'Currently there are no rooms.'
            msg += 'Please create a room before adding a person.'
            msg += 'This is for purposes of random allocation.'
            click.secho(msg, fg='red')
            return 'No rooms added for random allocation.'
        person_type = person_type.title()
        if not self.people:
            if person_type == 'Fellow':
                f_id = 1
                self.f_ids.append(f_id)
                identifier = 'F' + str(f_id)
                person = Fellow(first_name, other_name)
                person.get_full_name()
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type == 'Staff':
                s_id = 1
                self.s_ids.append(s_id)
                identifier = 'S' + str(s_id)
                person = Staff(first_name, other_name)
                person.get_full_name()
                person.assign_identifier(identifier)
                self.staff.append(person.full_name)
        else:
            if person_type == 'Fellow':
                person = Fellow(first_name, other_name)
                person.get_full_name()
                f_id = self.f_ids.pop() + 1
                identifier = 'F' + str(f_id)
                self.f_ids.append(f_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type == 'Staff':
                person = Staff(first_name, other_name)
                person.get_full_name()
                s_id = self.s_ids.pop() + 1
                identifier = 'S' + str(s_id)
                self.s_ids.append(s_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
        self.people.append(person)
        click.secho('The %s %s has been created.\n' %
                    (person.person_type, person.full_name), fg='green', bold=True)
        click.secho('ALLOCATING ROOM ...', fg='cyan')
        time.sleep(2)
        click.secho('Success!', fg='green')
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        if person_type == 'Staff':
            staff_single_allocation = {}
            staff_single_allocation[person.full_name] = self.offices['available'][
                randint(0, (len(self.offices['available']) - 1))]
            self.staff_allocations.append(staff_single_allocation)
            for room in self.rooms:
                if room.room_name == staff_single_allocation[person.full_name]:
                    if room.capacity > 0:
                        room.capacity = room.add_person(person.full_name)
                    else:
                        self.offices['available'].remove(room.room_name)
                        self.offices['unavailable'].append(room.room_name)
        if person_type == 'Fellow':
            if accomodate.upper() == 'Y':
                fellow_single_allocation = {}
                fellow_single_allocation['name'] = person.full_name
                fellow_single_allocation['office'] = self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                fellow_single_allocation['living_space'] = self.living_spaces['available'][
                    randint(0, (len(self.living_spaces['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == fellow_single_allocation['office']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)
                    elif room.room_name == fellow_single_allocation['living_space']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.living_spaces[
                                'available'].remove(room.room_name)
                            self.living_spaces[
                                'unavailable'].append(room.room_name)
            else:
                fellow_single_allocation = {}
                fellow_single_allocation[person.full_name] = self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == fellow_single_allocation[person.full_name]:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)

    def reallocate_person(self, person_id, room_name):
        if type(room_name) != str:
            return 'Error. Please enter valid room name.'
        person_id = person_id.upper()
        room_name = room_name.title()
        all_person_ids = []
        for person in self.people:
            all_person_ids.append(person.identifier)
            if person.identifier == person_id:
                person_name = person.full_name
        if person_id not in all_person_ids:
            click.secho('Person ID entered does not exist.',
                        fg='red', bold=True)
            return "Invalid person  type."
        for room in self.rooms:
            if person_name in room.occupants:
                current_room = room.room_name
                room.occupants.remove(person_name)

        # Reallocate to actual room
        for room in self.rooms:
            if room.room_name == room_name and room.capacity > 0:
                room.capacity = room.add_person(person_name)
                click.secho('%s has been reallocated from %s to %s.' %
                        (person_name, current_room, room.room_name),
                        fg='green', bold=True)
                return 'Person reallocated tp %s' % room_name

# amity = Amity()
# amity.create_room('o', 'Oculus')
# amity.create_room('o', 'MODOR')
# amity.add_person('Kimani', 'Ndegwa', 'Fellow')
# amity.add_person('eDWARD', 'KARANJA', 'Fellow')
# amity.add_person('eDWARD', 'KARANJA', 'STAFF')
# amity.print_allocations()
# print(amity.people)
# for p in amity.people:
#     print(p.identifier)
# amity.reallocate_person('F1', 'Modor')
