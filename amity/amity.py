import os
import time
import click
from random import randint
from rooms.room import LivingSpace, Office
from people.person import Fellow, Staff
from db.models import People, Rooms, DatabaseManager, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
        # self.rooms = self.offices['available']
        self.fellows = []
        self.staff = []
        self.people = self.staff + self.fellows
        self.f_ids = [0]
        self.s_ids = [0]
        # # Regarding allocations
        self.staff_allocations = []
        self.fellow_allocations = []
        self.unallocated_persons = []

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
        if room_type.upper() == 'O':
            room_type = 'Office'
        if room_type.upper() == 'L':
            room_type = 'Living Space'
        for room in self.rooms:
            if room.room_name == room_name.title() and \
                    room.room_type == room_type.title():
                click.secho('%s --> %s ALREADY EXISTS.Please pick another name.'
                            % (room_type, room_name.title()),
                            fg='red', bold=True)
                return 'Room already exists.'
        room_type = room_type.strip().title()
        room_name = room_name.strip().title()
        if room_type == 'Office':
            room = Office(room_name)
            self.offices['available'].append(room.room_name)
        elif room_type == 'Living Space':
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
            click.secho('==' * 30, fg='cyan')
            click.secho(room.room_name + '(' + room.room_type + ')',
                        fg='cyan')
            click.secho('==' * 30, fg='cyan')
            if room.occupants:
                for occupant in room.occupants:
                    click.secho(occupant)
            else:
                click.secho(
                    'There are no people in this room yet.', fg='cyan')

    def add_person(self, first_name, other_name, person_type,
                   accomodate='N'):
        # import ipdb;ipdb.set_trace()
        if type(first_name) != str or type(other_name) != str:
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        if first_name.isalpha() is False or other_name.isalpha() is False:
            click.secho('Person names need be alphabetical in nature',
                        fg='red', bold=True)
            return 'Non-Alphabetical names added'
        if person_type.title() not in ['Fellow', 'Staff']:
            click.secho('Please enter either Fellow or Staff for person type',
                        fg='red', bold=True)
            return 'Invalid Person Type'
        if accomodate.upper() not in ['Y', 'N']:
            click.secho('Please enter Y or N for wants accomodation.',
                        fg='red', bold=True)
            return 'Wants accomodation not Y or N'
        accomodate = accomodate.upper()
        person_type = person_type.title()
        if person_type == 'Staff' and accomodate == 'Y':
            click.secho(
                'A Staff member cannot be allocated accomodation.',
                fg='red', bold=True)
            return 'Staff cannot have wants accomodation of Y.'
        fn = first_name.title() + ' ' + other_name.title()
        for person in self.people:
            if person.full_name == fn and \
                    person.person_type == person_type.title():
                click.secho('%s %s ALREADY EXISTS.' % (person_type, fn))
                return 'Person exists.'
        if not self.living_spaces['available'] and not \
                self.offices['available']:
            click.secho(
                'THERE ARE NO ROOMS IN THE SYSTEM YET OR ALL ROOMS ARE FULL.',
                fg='red', bold=True)
            return 'There are no rooms in the system.'
        # if not self.living_spaces['available'] and accomodate == 'Y':
        #     click.secho(
        #         'There are no available living spaces at the moment. Please add one.')
        #     return 'No living spaces'
        # if not self.offices['available'] and accomodate == 'Y':
        #     click.secho('No offices available at the moment. Please add one')
        #     return 'No office'

        if accomodate == 'Y' and person_type == 'Fellow':
            if not self.living_spaces['available']:
                click.secho(
                    'Please add a living space for a fellow to be allocated both room types.',
                    fg='red', bold=True)
                return 'No Living space for fellow requiring both.'
            elif not self.offices['available']:
                click.secho(
                    'Please add an office for a fellow to be allocated both room types.',
                    fg='red', bold=True)
                return 'No office for fellow requiring both.'
        # if not self.rooms:
        #     msg = 'Currently there are no rooms.'
        #     msg += 'Please create a room before adding a person.'
        #     msg += 'This is for purposes of random allocation.'
        #     click.secho(msg, fg='red')
        #     return 'No rooms added for random allocation.'
        if not self.people:
            if person_type.title() == 'Fellow':
                f_id = 1
                self.f_ids.append(f_id)
                identifier = 'F' + str(f_id)
                person = Fellow(first_name, other_name)
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                s_id = 1
                self.s_ids.append(s_id)
                identifier = 'S' + str(s_id)
                person = Staff(first_name, other_name)
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.staff.append(person.full_name)
        else:
            if person_type.title() == 'Fellow':
                person = Fellow(first_name, other_name)
                person.accomodate = accomodate
                person.get_full_name()
                f_id = self.f_ids.pop() + 1
                identifier = 'F' + str(f_id)
                self.f_ids.append(f_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                person = Staff(first_name, other_name)
                person.accomodate = accomodate
                person.get_full_name()
                s_id = self.s_ids.pop() + 1
                identifier = 'S' + str(s_id)
                self.s_ids.append(s_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
        self.people.append(person)
        click.secho('The %s %s has been created.\n' %
                    (person.person_type, person.full_name),
                    fg='green', bold=True)
        click.secho('ALLOCATING ROOM ...', fg='cyan')
        time.sleep(1)
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
                        click.secho('Success!', fg='green')
                        room.capacity = room.add_person(person.full_name)
                    else:
                        self.offices['available'].remove(room.room_name)
                        self.offices['unavailable'].append(room.room_name)
                        self.unallocated_persons.append(person.full_name)
                        msg = '%s has reached its Maximum capacity.' % room.room_name
                        msg += 'Please add another %s.' % room.room_type
                        click.secho(msg, fg='red', bold=True)

        if person_type == 'Fellow':
            if accomodate == 'Y':
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
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)
                    elif room.room_name == fellow_single_allocation['living_space']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.living_spaces[
                                'available'].remove(room.room_name)
                            self.living_spaces[
                                'unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)
                click.secho('Success!', fg='green')
                return 'Fellow allocated both living space and office'
            else:
                fellow_single_allocation = {}
                fellow_single_allocation[person.full_name] = \
                    self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == \
                            fellow_single_allocation[person.full_name]:
                        if room.capacity > 0:
                            click.secho('Success!', fg='green')
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)

    def get_identifier(self, first_name, last_name):
        """
        The get identfier method intends to get a person's
        id to be able to reallocate them appropriately.
        """
        if not self.people:
            click.secho('There are Currently no people in the system.')
            return 'No people added'
        else:
            fn = first_name.title() + ' ' + last_name.title()
            for person in self.people:
                if person.full_name == fn:
                    msg = click.secho(person.identifier, fg='green')
                    return person.identifier
            else:
                msg = click.secho('Person does not exist.', fg='red')
                return msg

    def reallocate_person(self, person_id, room_name):
        '''
        The beginning of the method validates of the data passed
        is a string and then proceeds to take the person_id and
        accordingly reallocate them.
        PERSON_ID which in this case is the identifier
        is converted to upper case.
        '''
        available_rooms = []
        if type(room_name) != str:
            return 'Error. Please enter valid room name.'
        for room in self.offices['available']:
            available_rooms.append(room)
        for room in self.living_spaces['available']:
            available_rooms.append(room)
        person_id = person_id.upper()
        room_name = room_name.title()
        for person in self.people:
            if person.full_name in self.unallocated_persons and person.identifier == person_id:
                click.secho('Person is not allocated. Please use --->reallocate unallocated',
                            fg='yellow', bold=True)
                return 'unallocated person.'
        if room_name.title() not in available_rooms:
            click.secho('Room name %s does not exist.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'
        for person in self.people:
            if person.accomodate == 'N' and person.identifier == person_id:
                if room_name in self.living_spaces['available']:
                    click.secho(
                        'Cant move fellow from office to living space',
                        fg='red', bold=True)
                    return 'Fellow does not want accomodation'
        all_person_ids = []
        for person in self.people:
            all_person_ids.append(person.identifier)
            if person.identifier == person_id:
                person_name = person.full_name
        if person_id not in all_person_ids:
            click.secho('Person ID entered does not exist.',
                        fg='red', bold=True)
            return "Invalid person id."
        for person in self.people:
            if person.identifier == person_id:
                wanted_name = person.full_name
        for room in self.rooms:
            if wanted_name in room.occupants and \
                    room.room_name == room_name:
                click.secho('You cannot be reallocated to the same room.',
                            fg='red', bold=True)
                return 'cant reallocate to same room'
        if room_name in self.offices['available']:
            room_t = 'Office'
        if room_name in self.living_spaces['available']:
            room_t = 'Living Space'
        for room in self.rooms:
            if person_name in room.occupants and room_t == room.room_type:
                current_room = room.room_name
                room.occupants.remove(person_name)

        # Reallocate to actual room
        for room in self.rooms:
            if room.room_name == room_name and room.capacity > 0:
                room.capacity = room.add_person(person_name)
                click.secho('%s has been reallocated from %s to %s.' %
                            (person_name, current_room, room.room_name),
                            fg='green', bold=True)
                return 'Person reallocated to %s' % room_name

    def reallocate_unallocated(self, person_id, room_name):
        # Reallocate someone who is in the unallocated section
        available_rooms = []
        if type(room_name) != str:
            return 'Error. Please enter valid room name.'
        room_name = room_name.title()
        person_id = person_id.upper()
        people_ids = []
        for person in self.people:
            people_ids.append(person.identifier)
        if person_id not in people_ids:
            click.secho('Person ID does not exist', fg='red', bold=True)
            return 'Person ID does not exist.'

        for room in self.offices['available']:
            available_rooms.append(room)
        for room in self.living_spaces['available']:
            available_rooms.append(room)
        if room_name.title() not in available_rooms:
            click.secho('Room name %s does not exist.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'
        for person in self.people:
            if person.full_name in self.unallocated_persons and \
                    person.identifier == person_id:
                unallocated_person = person.full_name
        for room in self.rooms:
            if room.room_name == room_name:
                room.occupants.append(unallocated_person)
                self.unallocated_persons.remove(unallocated_person)
                click.secho('%s reallocated to %s' % (
                    unallocated_person, room_name), fg='green', bold=True)

    def print_room(self, room_name):
        '''
        This function gets a room name as an argument and proceeds
        to display the results on the occupants of the room if any.
        '''
        if not self.rooms:
            click.secho('THERE ARE NO ROOMS IN THE SYSTEM YET.',
                        fg='red', bold=True)
            return 'No rooms exist at the moment.'
        all_rooms = []
        for room in self.rooms:
            all_rooms.append(room.room_name)
        if room_name.title() not in all_rooms:
            click.secho('The room %s does not exist on our system.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'

        room_name = room_name.title()
        for room in self.rooms:
            if room.room_name == room_name:
                click.secho('ROOM NAME:%s(%s)' %
                            (room_name, room.room_type),
                            fg='yellow', bold=True)
                click.secho('=' * 20, fg='cyan')
                if room.occupants:
                    for occupant in room.occupants:
                        click.secho(occupant, fg='yellow')
                else:
                    click.secho('Its lonely here.', fg='cyan', bold=True)
                    return False

    def print_unallocated(self):
        '''
        After Max capacity has been recorded in a particular
        room, the person is thereafter appended to a the unallocated
        persons list.
        '''
        if not self.unallocated_persons:
            click.secho('There are no unallocated people as of now.',
                        fg='green', bold=True)
            return 'No unallocated people as per now.'
        else:
            click.secho('UNALLOCATED PEOPLE IN MY AMITY.', fg='red', bold=True)
            for unallocated in self.unallocated_persons:
                click.secho(unallocated, fg='yellow')
                return 'Some people unallocated.'

    def save_state(self):
        if os.path.exists('default_amity_db.sqlite'):
            os.remove('default_amity_db.sqlite')
        db = DatabaseManager()
        Base.metadata.bind = db.engine
        s = db.session()
        # import ipdb; ipdb.set_trace()
        try:
            for person in self.people:
                for room in self.rooms:
                    if person.full_name in room.occupants:
                        if room.room_type == 'Office':
                            office_allocated = room.room_name
                        if room.room_type == 'Living Space' and \
                                person.accomodate == 'Y':
                            ls_allocated = room.room_name
                        else:
                            ls_allocated = None
                    if person.full_name in self.unallocated_persons:
                        ls_allocated = 'Unallocated'
                        office_allocated = 'Unallocated'
                person_to_db = People(
                    person_identifier=person.identifier,
                    person_name=person.full_name,
                    person_type=person.person_type,
                    wants_accomodation=person.accomodate,
                    office_allocated=office_allocated,
                    living_space_allocated=ls_allocated
                )
                s.merge(person_to_db)

            for room in self.rooms:
                room_to_db = Rooms(
                    room_name=room.room_name,
                    room_type=room.room_type,
                    room_capacity=room.capacity,
                )
                s.merge(room_to_db)
            s.commit()
            message = "Data added to {} database successfully".\
                format(db.db_name.upper())
            click.secho(message, fg='green', bold=True)
            return True
        except Exception as e:
            print(e)
            return "Error encountered when adding people to db."

    def load_state(self):
        '''
        This function queries from the database and contiues the
        seesion from that point as expected.

        '''
        engine = create_engine('sqlite:///default_amity_db.sqlite')
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        all_people = session.query(People).all()
        all_rooms = session.query(Rooms).all()
        for r in all_rooms:
            if r.room_type == 'Office':
                room = Office(r.room_name)
                if r.room_capacity > 0:
                    self.offices['available'].append(r.room_name)
                else:
                    self.offices['unavailable'].append(r.room_name)
            if r.room_type == 'Living Space':
                room = LivingSpace(r.room_name)
                if r.room_capacity > 0:
                    self.living_spaces['available'].append(r.room_name)
                else:
                    self.living_spaces['unavailable'].append(r.room_name)
            self.rooms.append(room)
        for p in all_people:
            if not self.people:
                if p.person_type == 'Fellow':
                    full_name = p.person_name.split()
                    person = Fellow(full_name[0], full_name[1])
                    f_id = 1
                    self.f_ids.append(f_id)
                    identifier = 'F' + str(f_id)
                    person.identifier = identifier
                    person.accomodate = p.wants_accomodation
                    person.get_full_name()
                    self.fellows.append(person.full_name)
                elif p.person_type == 'Staff':
                    full_name = p.person_name.split()
                    person = Staff(full_name[0], full_name[1])
                    s_id = 1
                    self.s_ids.append(s_id)
                    identifier = 'S' + str(s_id)
                    person.identifier = identifier
                    person.accomodate = p.wants_accomodation
                    person.get_full_name()
                    self.staff.append(person.full_name)
            else:
                if p.person_type == 'Fellow':
                    full_name = p.person_name.split()
                    person = Fellow(full_name[0], full_name[1])
                    f_id = self.f_ids.pop() + 1
                    identifier = 'F' + str(f_id)
                    self.f_ids.append(f_id)
                    person.accomodate = p.wants_accomodation
                    person.identifier = identifier
                    person.get_full_name()
                    self.fellows.append(person.full_name)
                elif p.person_type == 'Staff':
                    full_name = p.person_name.split()
                    person = Staff(full_name[0], full_name[1])
                    s_id = self.s_ids.pop() + 1
                    identifier = 'S' + str(s_id)
                    person.identifier = identifier
                    self.s_ids.append(s_id)
                    person.accomodate = p.wants_accomodation
                    person.get_full_name()
                    self.fellows.append(person.full_name)
            self.people.append(person)
            # Append person object to people list.
            for room in self.rooms:
                if p.living_space_allocated == room.room_name:
                    room.add_person(p.person_name)
                elif p.office_allocated == room.room_name:
                    room.add_person(p.person_name)
