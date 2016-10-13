import click
from random import randint
from rooms.room import LivingSpace, Office
from people.person import Fellow, Staff
from rooms.room import LivingSpace, Office


class Amity(object):
    def __init__(self):
        self.all_rooms = []
        self.offices = []
        self.living_spaces = []
        self.rooms = {
            'offices': self.offices,
            'living_spaces': self.living_spaces
        }
        # Regarding People
        self.fellows = []
        self.staff = []

        self.people = {
            'fellows': self.fellows,
            'staff': self.staff

        }

        self.people_stats = []
        self.f_ids = [0]
        self.s_ids = [0]
        # Regarding allocations
        self.staff_allocations = []
        self.fellow_allocations = []

    def create_room(self, room_type, room_name):
        if type(room_type) != str or room_type.upper() not in ['O', 'L']:
            return 'Please enter O or L for a room'
        single_room = {}
        if room_type.upper() == 'O':
            office = Office()
            single_room['room_name'] = room_name
            single_room['room_type'] = office.room_type
            single_room['room_capacity'] = office.capacity
            single_room['occupants'] = []
            self.offices.append(room_name)
        elif room_type.upper() == 'L':
            living = LivingSpace()
            single_room['room_name'] = room_name
            single_room['room_type'] = living.room_type
            single_room['room_capacity'] = living.capacity
            single_room['occupants'] = []
            self.living_spaces.append(room_name)
        self.all_rooms.append(single_room)
        return 'The room %s has been created.' % room_name

    def print_allocations(self):
        for room_index in range(len(self.all_rooms)):
            if self.all_rooms[room_index]['occupants']:
                click.secho(self.all_rooms[room_index]['room_name'])
                click.secho('==' * 10, fg='cyan')
                for occupant in self.all_rooms[room_index]['occupants']:
                    click.secho(occupant)
            else:
                click.secho(self.all_rooms[room_index][
                            'room_name'], fg='yellow')
                click.secho('==' * 20)
                click.secho(
                    'There are no occupants in this room yet.', fg='red')

    def add_person(self, name, person_type, wants_accomodation='N'):
        if type(name) != str or type(person_type) != str:
            return 'Wrong format for name or person type'
        if person_type not in ['Fellow', 'Staff']:
            return 'Please enter Fellow or Staff for person type.'
        if wants_accomodation.upper() not in ['Y', 'N']:
            return 'Please enter Y or N for wants accomodation.'
        if person_type == 'Staff' and wants_accomodation == 'Y':
            return 'A Staff member cannot be allocated accomodation.'
        if bool(self.all_rooms) is False:
            msg = 'Currently there are no rooms.'
            msg += 'Please create a room before adding a person.'
            msg += 'This is for purposes of random allocation.'
            return msg
        person_stats = {}
        person_stats['name'] = name
        person_stats['wants_accomodation'] = wants_accomodation

        if bool(self.people_stats) is False:
            if person_type == 'Fellow':
                fellow = Fellow()
                f_id = 1
                self.f_ids.append(f_id)
                person_stats['person_id'] = 'F' + str(f_id)
                person_stats['person_type'] = fellow.person_type
                self.fellows.append(name)
            elif person_type == 'Staff':
                staff = Staff()
                s_id = 1
                self.s_ids.append(s_id)
                person_stats['person_id'] = 'S' + str(s_id)
                person_stats['person_type'] = staff.person_type
                self.staff.append(name)
        else:
            if person_type == 'Fellow':
                fellow = Fellow()
                f_id = self.f_ids.pop() + 1
                person_stats['person_id'] = 'F' + str(f_id)
                person_stats['person_type'] = fellow.person_type
                self.f_ids.append(f_id)
                self.fellows.append(name)
            elif person_type == 'Staff':
                staff = Staff()
                s_id = self.s_ids.pop() + 1
                person_stats['person_id'] = 'S' + str(s_id)
                person_stats['person_type'] = staff.person_type
                self.s_ids.append(s_id)
                self.staff.append(name)
        self.people_stats.append(person_stats)
        msg = 'The %s %s has been created.' % (person_type, name)
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        if person_type == 'Staff':
            staff_single_allocation = {}
            staff_single_allocation[name] = self.offices[
                randint(0, (len(self.offices) - 1))]
            self.staff_allocations.append(staff_single_allocation)
            for r in range(len(self.all_rooms)):
                if self.all_rooms[r]['room_name'] == staff_single_allocation[name]:
                    self.all_rooms[r]['occupants'].append(name)
        elif person_type == 'Fellow':
            if wants_accomodation == 'Y':
                fellow_single_allocation = {}
                fellow_single_allocation['name'] = name
                fellow_single_allocation['office'] = self.offices[
                    randint(0, (len(self.offices) - 1))]
                fellow_single_allocation['living_space'] = self.living_spaces[
                    randint(0, (len(self.living_spaces) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for r in range(len(self.all_rooms)):
                    if self.all_rooms[r]['room_name'] == fellow_single_allocation['office']:
                        self.all_rooms[r]['occupants'].append(name)
                    elif self.all_rooms[r]['room_name'] == fellow_single_allocation['living_space']:
                        self.all_rooms[r]['occupants'].append(name)
            else:
                fellow_single_allocation = {}
                fellow_single_allocation[name] = self.offices[
                    randint(0, (len(self.offices) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for r in range(len(self.all_rooms)):
                    if self.all_rooms[r]['room_name'] == fellow_single_allocation[name]:
                        self.all_rooms[r]['occupants'].append(name)
        return 'person has been created'

        def reallocate_person(self, person_id, room_name):
            if type(room_name) != str:
                return 'Error. Please enter valid room name.'

            people_ids = []
            for p in range(len(self.people_stats)):
                if self.people_stats[p]['person_id']:
                    people_ids.append(self.people_stats[p]['person_id'])
            if person_id not in people_ids:
                return 'Error. The person you entered does not exist in our system.'
            amity_rooms = []
            for office in self.offices:
                amity_rooms.append(office)
            for living_space in self.living_spaces:
                amity_rooms.append(living_space)
            if room_name not in amity_rooms:
                return 'Error. The room name you entered does not exist on our system.'
            #find out first where a person is allocated
            #remove them from that list / dictionary
            #reallocate them as need be
            # if person_id.startswith('S'):
            #     if staff_allocations['']

        # except Exception as e:
        #     print(e)
        #     return 'An error occurred'


amity = Amity()
amity.create_room('O', 'Krypton')
amity.create_room('O', 'Oculus')
# amity.create_room('O', 'Narnia')
# amity.create_room('O', 'Vahalla')
amity.create_room('L', 'PHP')
amity.create_room('L', 'Ruby')
# amity.create_room('L', 'Haskell')
# amity.create_room('L', 'Python')

# # amity.create_room('L', 'Oculus')
# # print(amity.all_rooms)
# # amity.print_allocations()
amity.add_person('kIMANI nDEGWA', 'Fellow')
# amity.add_person('kamau dungu', 'Staff')
# # print(amity.add_person('KINJA KARIUKI', 'Staff'))

print(amity.people_stats)
# print(amity.all_rooms)
print(amity.staff_allocations)
print(amity.fellow_allocations)
# amity.print_allocations()

