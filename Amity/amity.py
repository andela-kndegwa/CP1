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
                identifier = 'F' + str(s_id)
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
                            self.living_spaces['available'].remove(room.room_name)
                            self.living_spaces['unavailable'].append(room.room_name)
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


    # def allocate_room(self, person_name, person_type, accomodate=False):
    #     if not self.offices:
    #         return 'Please add an office'
    #     for room in self.all_rooms:
    #         if len(room['occupants']) == 4:
    #             self.offices['unavailable'].append(room)
    #             return 'Unavailable room.'
    #     for

    # def reallocate_person(self, person_id, room_name):
    #     if type(room_name) != str:
    #         return 'Error. Please enter valid room name.'

    #     people_ids = []
    #     for p in range(len(self.people_stats)):
    #         if self.people_stats[p]['person_id']:
    #             people_ids.append(self.people_stats[p]['person_id'])
    #     if person_id not in people_ids:
    #         return 'Error. The person you entered does not exist in our system.'
    #     amity_rooms = []
    #     for office in self.offices:
    #         amity_rooms.append(office)
    #     for living_space in self.living_spaces:
    #         amity_rooms.append(living_space)
    #     if room_name not in amity_rooms:
    # return 'Error. The room name you entered does not exist on our system.'

    #     # find out first where a person is allocated
    #     # remove them from that list / dictionary
    #     # reallocate them as need be
    #     for p in range(len(self.people_stats)):
    #         if self.people_stats[p]['person_id'] == person_id:
    #             found_name_in_old_room = self.people_stats[p]['name']
    #             for r in range(len(self.all_rooms)):
    #                 if found_name_in_old_room in self.all_rooms[r]['occupants']:
    #                     self.all_rooms[r]['occupants'].remove(
    #                         found_name_in_old_room)
    #                 if room_name == self.all_rooms[r]['room_name']:
    #                     self.all_rooms[r]['occupants'].append(
    #                         found_name_in_old_room)
    # return 'Success! %s has been reallocated to %s ' %
    # (found_name_in_old_room.title(), room_name)

    #         # except Exception as e:
    #         #     print(e)
    #         #     return 'An error occurred'
    # def print_room(self, room_name):
    #     for r in range(len(self.all_rooms)):
    #         if self.all_rooms[r]['room_name'] == room_name:
    #             click.secho('Room Name : %s\n ' % room_name, fg='yellow')
    #             if self.all_rooms[r]['occupants']:
    #                 for occupant in self.all_rooms[r]['occupants']:
    #                     click.secho('=' * 10, fg='cyan')
    #                     click.secho(occupant)
    #             else:
    #                 click.secho(
    #                     'There are no occupants in this room as per now.', fg='yellow')


# amity = Amity()
# amity.create_room('o', 'Swift')
# amity.create_room('o', 'oculus')
# amity.create_room('o', 'krypton')
# amity.add_person('Kimani', 'nDEGWA', 'Fellow', 'N')
# amity.print_allocations()
# print(amity.offices)
