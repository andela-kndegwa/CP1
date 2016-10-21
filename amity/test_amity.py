import os
import unittest
from mock import patch
from amity import Amity


class TestAmityFunctionality(unittest.TestCase):
    '''
    The self.amity Class here is used to hold the mian functionality
    of the self.amity Room Allocation system. It imports and makes calls
    to all other classes and manages them to create necessary instances
    and performs the necessary logic. This Test Class thus tests
    all the logic approporately.
    '''

    def setUp(self):
        self.amity = Amity()

    def test_amity_class_initialises_with_nothing(self):
        self.assertEquals(len(self.amity.rooms), 0)
        self.assertEquals(len(self.amity.people), 0)
        self.assertEquals(len(self.amity.fellows), 0)
        self.assertEquals(len(self.amity.staff), 0)

    # create room method test functionality begins here
    def test_returns_error_when_non_string_is_addded(self):
        self.assertEqual(self.amity.create_room(
            0, 2), 'Error. Invalid room type initial.',
            msg='Room name and initial must only be strings.')
        self.assertEqual(self.amity.create_room('w', 'WorkSpace'),
                         'Error. Invalid room type initial.',
                         msg='Enter O or L for room type inital.')

    def test_create_room_method(self):
        with patch("amity.rooms.room.Office"):
            self.amity.create_room("o", "Lime")
            self.assertIn("Lime", self.amity.offices['available'])
        with patch("amity.rooms.room.LivingSpace"):
            self.amity.create_room('l', 'python')
            self.assertIn('Python', self.amity.living_spaces['available'])

    def test_create_room_increases_rooms_list_by_one(self):
        room_count_before = len(self.amity.rooms)
        with patch("amity.rooms.room.Office"):
            self.amity.create_room("o", "Lime")
            room_count_after = len(self.amity.rooms)
            self.assertEquals((room_count_after - room_count_before), 1)
            self.amity.create_room('o', 'oculus')
            room_count_after_two = len(self.amity.rooms)
            self.assertAlmostEquals(
                (room_count_after_two - room_count_before), 2)

    def test_living_space_can_only_be_created_once(self):
        with patch('amity.rooms.room.LivingSpace'):
            self.amity.create_room('l', 'ruby')
            result = self.amity.create_room('l', 'ruby')
            self.assertEqual(result, 'Room already exists.')

    def test_office_can_only_be_created_once(self):
        with patch('amity.rooms.room.Office'):
            self.amity.create_room('o', 'orange')
            result = self.amity.create_room('o', 'orange')
            self.assertEqual(result, 'Room already exists.')

    def test_room_creation_when_successful(self):
        with patch('amity.rooms.room.Office'):
            result = self.amity.create_room('o', 'krypton')
            self.assertEqual(result, 'Room Krypton created.')
        with patch('amity.rooms.room.LivingSpace'):
            result = self.amity.create_room('l', 'haskell')
            self.assertEqual(result, 'Room Haskell created.')

    # Print allocations method test begins here
    def test_returns_no_allocations_if_no_rooms_created(self):
        self.assertEqual(self.amity.print_allocations(),
                         'Error. No rooms within system.')
    # add_person method testing begins here

    def test_returns_error_if_no_rooms_within_system(self):
        result = self.amity.add_person('Jackie', 'Maribe', 'Fellow', 'Y')
        self.assertEqual(result, 'There are no rooms in the system.')

    def test_validation_of_people_names(self):
        self.amity.create_room('o', 'lime')
        res = self.amity.add_person('Jackie', 45, 'Fellow', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Wrong type for name.')
        res2 = self.amity.add_person('J6327', 'Maribe', 'Fellow', 'Y')
        self.assertTrue(res2)
        self.assertEqual(res2, 'Non-Alphabetical names added')

    def test_validation_of_people_types(self):
        self.amity.create_room('o', 'cyan')
        res = self.amity.add_person('alex', 'graham', 'worker', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Invalid Person Type')

    def test_staff_cannot_want_accomodation(self):
        self.amity.create_room('l', 'ruby')
        res = self.amity.add_person('alex', 'graham', 'staff', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Staff cannot have wants accomodation of Y.')

    def test_wants_accomodation_is_either_y_or_n(self):
        self.amity.create_room('o', 'lilac')
        res = self.amity.add_person('seralynnette', 'nduta', 'Fellow', 'Yes')
        self.assertTrue(res)
        self.assertEqual(res, 'Wants accomodation not Y or N')

    def test_validation_if_person_fellow_and_wants_accomodation(self):
        '''
        Both a living space and office must exist for a fellow who
        wants accomodation.
        '''
        self.amity.create_room('o', 'pyrex')
        res = self.amity.add_person('wycliffe', 'wangondu', 'Fellow', 'Y')
        self.assertTrue(res)
        self.assertEqual(res, 'No Living space for fellow requiring both.')

    def test_passes_validation_and_creates_person(self):
        # Since there are only two rooms: one of each Living Space and Office
        # and person wants accomodation
        # we are sure the rooms allocated are as created.
        self.amity.create_room('o', 'clandy')
        self.amity.create_room('l', 'calself.amity')
        self.amity.add_person('myanmar', 'wakesho', 'Fellow', 'y')
        for room in self.amity.rooms:
            if room.room_name == 'Clandy':
                self.assertIn('Myanmar Wakesho', room.occupants)
                self.assertEqual(len(room.occupants), 1)
            if room.room_name == 'Calself.amity':
                self.assertIn('Myanmar Wakesho', room.occupants)
                self.assertEqual(len(room.occupants), 1)

    def test_person_objects_are_created(self):
        self.amity.create_room('o', 'mars')
        self.amity.create_room('l', 'earth')
        self.amity.add_person('justine', 'kariuki', 'Fellow', 'y')
        for person in self.amity.people:
            if person.full_name == 'Justine Kariuki':
                self.assertEqual(person.person_type, 'Fellow')
                self.assertEqual(person.identifier, 'F1')

        self.amity.add_person('alec', 'kambua', 'Staff', 'n')
        for person in self.amity.people:
            if person.full_name == 'Alec Kambua':
                self.assertEqual(person.person_type, 'Staff')
                self.assertEqual(person.identifier, 'S1')

    def test_get_identifier_if_no_people_added(self):
        self.assertEqual(self.amity.get_identifier(
            'Lydiah', 'Kan'), 'No people added')

    def test_get_identifier_if_people_added(self):
        self.amity.create_room('o', 'yellow')
        self.amity.create_room('l', 'blue')
        self.amity.add_person('brandon', 'balagu', 'Fellow', 'y')
        self.assertEqual(self.amity.get_identifier(
            'brandon', 'balagu'), 'F1')
    # Test Reallocate Person starts here

    def test_reallocate_person(self):
        self.amity.create_room('o', 'Jupiter')
        self.amity.create_room('o', 'Pluto')
        self.amity.add_person('isaac', 'kimani', 'staff', 'n')
        res = self.amity.reallocate_person('S1', [])
        self.assertEqual(res, "Error. Please enter valid room name.")

    def test_reallocate_person_when_room_does_not_exist(self):
        self.amity.create_room('o', 'Mars')
        self.amity.create_room('o', 'Venus')
        self.amity.add_person('Nduta', 'Nungari', 'staff', 'n')
        res = self.amity.reallocate_person('S1', 'Neptune')
        self.assertEqual(res, "Room does not exist.")

    def test_reallocate_person_when_person_accomodate_is_N(self):
        self.amity.create_room('o', 'Mars')
        self.amity.create_room('l', 'Venus')
        self.amity.add_person('Xander', 'Akura', 'Fellow', 'n')
        res = self.amity.reallocate_person('F1', 'Venus')
        self.assertEqual(res, 'Fellow does not want accomodation')
        for room in self.amity.rooms:
            if room.room_name == 'Venus':
                self.assertNotIn('Xander Akura', room.occupants)

    def test_reallocate_to_same_room(self):
        self.amity.create_room('o', 'Mars')
        self.amity.add_person('michelle', 'wanjiru', 'Fellow', 'n')
        res = self.amity.reallocate_person('F1', 'Mars')
        self.assertEqual(res, 'cant reallocate to same room')

    def test_reallocate_to_same_room_if_person_id_non_exitent(self):
        self.amity.create_room('o', 'Mars')
        self.amity.create_room('o', 'Venus')
        self.amity.add_person('serallynnette', 'wanjiku', 'Staff', 'n')
        res = self.amity.reallocate_person('Staff1', 'Mars')
        self.assertEqual(res, 'Invalid person id.')

    def test_reallocate_person_works(self):
        self.amity.create_room('o', 'valhalla')
        self.amity.add_person('seralynnette', 'wanjiku', 'Staff', 'n')
        self.amity.create_room('o', 'narnia')
        res = self.amity.reallocate_person('S1', 'narnia')
        self.assertEqual(res, 'Person reallocated to Narnia')
        for room in self.amity.rooms:
            if room.room_name == 'Valhalla':
                self.assertNotIn('Seralynnette Wanjiku', room.occupants)
            if room.room_name == 'Narnia':
                self.assertIn('Seralynnette Wanjiku', room.occupants)

    def test_reallocate_unallocated(self):
        self.amity.create_room('o', 'prayar')
        self.amity.add_person('Austin', 'Mugage', 'staff')
        res = self.amity.reallocate_unallocated('s65', 'Prayar')
        self.assertEqual(res, 'Person ID does not exist.')
    # test_print_room_works

    def test_print_room_if_no_rooms(self):
        res = self.amity.print_room('Jupite')
        self.assertEqual(res, 'No rooms exist at the moment.')

    def test_if_room_exists(self):
        self.amity.create_room('o', 'jupite')
        res = self.amity.print_room('SOHK')
        self.assertEqual(res, 'Room does not exist.')

    # test print unallocated
    def test_print_unallocated_if_all_allocated(self):
        self.amity.create_room('o', 'lyon')
        self.amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        res = self.amity.print_unallocated()
        self.assertEqual(res, 'No unallocated people as per now.')

    def test_print_unallocated_if_exisiting(self):
        self.amity.create_room('o', 'Witherspoon')
        self.amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        self.amity.unallocated_persons.append('Person Name')
        res = self.amity.print_unallocated()
        self.assertEqual(res, 'Some people unallocated.')
    # save state functionality

    def test_save_state(self):
        self.amity.create_room('o', 'Witherspoon')
        self.amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        self.assertFalse(os.path.exists('default_db_self.amity.sqlite'))

    def save_state_works(self):
        self.amity.create_room('o', 'Witherspoon')
        self.amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        res = self.amity.save_state()
        self.assertEqual(res, True)

    # additional tests
    def test_returns_correct_message(self):
        self.amity.create_room('o', 'hOGWARTS')
        self.amity.add_person('Bonnieface', 'Ntarangwi', 'Staff', 'n')
        res = self.amity.print_allocations()
        self.assertEqual(res, 'Print to screen')
        res2 = self.amity.print_allocations('test_bonnie')
        self.assertEqual(res2, 'Print to file')

    # test database loaded
    def test_database_loaded(self):
        self.amity.create_room('o', 'Hogwarts')
        self.amity.create_room('l', 'scala')
        self.amity.save_state()
        res = self.amity.load_state('default_amity_db')
        self.assertEqual(res, 'Database Loaded.')
