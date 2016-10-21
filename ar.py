import click
from random import randint
import time
from amity.people.person import Fellow, Staff


class Checker():
    def __init__(self):
        self.people = []
        self.rooms = []
        self.offices = {
            'available': [],
            'unavailable': []
        }
        self.living_spaces = {
            'available': [],
            'unavailable': []
        }

    def validate_person(self, first_name, other_name, person_type,
                        accomodate='N'):
        if type(first_name) != str or type(other_name) != str:
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        if not first_name.isalpha() or not other_name.isalpha():
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
            accomodate = 'N'
            click.secho(
                'A Staff member cannot be allocated accomodation.',
                fg='red', bold=True)
        fn = first_name.title() + ' ' + other_name.title()
        return [fn, accomodate, person_type]

    def validate_state_of_amity(self, validated_details):
        fn = validated_details[0]
        accomodate = validated_details[1]
        person_type = validated_details[2]
        for person in self.people:
            if person.full_name == fn and \
                    person.person_type == person_type.title():
                click.secho('%s %s ALREADY EXISTS.' % (person_type, fn))
                return 'Person exists.'
        if not self.offices['available'] and person_type == 'Staff':
            click.secho(
                'There are no offices or the offices are all full.',
                fg='red', bold=True)
            return 'There are no offices in the system.'
        if not self.living_spaces['available'] and not \
                self.offices['available']:
            click.secho(
                'THERE ARE NO ROOMS IN THE SYSTEM YET OR ALL ROOMS ARE FULL.',
                fg='red', bold=True)
            return 'There are no rooms in the system.'

        if accomodate == 'Y' and person_type == 'Fellow':
            if not self.living_spaces['available']:
                msg = 'Please add a living space for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                return 'No Living space for fellow requiring both.'
            elif not self.offices['available']:
                msg = 'Please add an office for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                return 'No office for fellow requiring both.'

    def generate_identifer(self, validated_details):
        fn = validated_details[0]
        accomodate = validated_details[1]
        person_type = validated_details[2]
        full_names = fn.split()
        if not self.people:
            if person_type.title() == 'Fellow':
                f_id = 1
                self.f_ids.append(f_id)
                identifier = 'F' + str(f_id)
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                s_id = 1
                self.s_ids.append(s_id)
                identifier = 'S' + str(s_id)
                person = Staff(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.staff.append(person.full_name)
        else:
            if person_type.title() == 'Fellow':
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                f_id = self.f_ids.pop() + 1
                identifier = 'F' + str(f_id)
                self.f_ids.append(f_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                person = Staff(full_names[0], full_names[1])
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

    def allocate_room(self, validated_details, person):
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        person_type = validated_details[0]
        accomodate = validated_details[1]
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


c = Checker()
res = c.validate_person('kimani', 'ndegwa', 'fellow')
res = c.validate_state_of_amity(res)
c.generate_identifer(res)
