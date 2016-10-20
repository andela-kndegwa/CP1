import unittest
from amity import Amity
from mock import patch, Mock


class TestAmityFunctionality(unittest.TestCase):
    '''
    The Amity Class here is used to hold the mian functionality
    of the Amity Room Allocation system. It imports and makes calls
    to all other classes and manages them to create necessary instances
    and performs the necessary logic. This Test Class thus tests
    all the logic approporately.
    '''

    def test_amity_class_initialises_with_nothing(self):
        amity = Amity()
        self.assertEquals(len(amity.rooms), 0)
        self.assertEquals(len(amity.people), 0)
        self.assertEquals(len(amity.fellows), 0)
        self.assertEquals(len(amity.staff), 0)

    # create room method test functionality begins here
    def test_returns_error_when_non_string_is_addded(self):
        amity = Amity()
        self.assertEqual(amity.create_room(
            0, 2), 'Error. Invalid room type initial.',
            msg='Room name and initial must only be strings.')
        self.assertEqual(amity.create_room('w', 'WorkSpace'),
                         'Error. Invalid room type initial.',
                         msg='Enter O or L for room type inital.')

    def test_create_room_method(self):
        amity = Amity()
        with patch("amity.rooms.room.Office"):
            amity.create_room("o", "Lime")
            self.assertIn("Lime", amity.offices['available'])
        with patch("amity.rooms.room.LivingSpace"):
            amity.create_room('l', 'python')
            self.assertIn('Python', amity.living_spaces['available'])

    def test_create_room_increases_rooms_list_by_one(self):
        amity = Amity()
        room_count_before = len(amity.rooms)
        with patch("amity.rooms.room.Office"):
            amity.create_room("o", "Lime")
            room_count_after = len(amity.rooms)
            self.assertEquals((room_count_after - room_count_before), 1)
            amity.create_room('o', 'oculus')
            room_count_after_two = len(amity.rooms)
            self.assertAlmostEquals(
                (room_count_after_two - room_count_before), 2)

    def test_living_space_can_only_be_created_once(self):
        amity = Amity()
        with patch('amity.rooms.room.LivingSpace'):
            amity.create_room('l', 'ruby')
            result = amity.create_room('l', 'ruby')
            self.assertEqual(result, 'Room already exists.')

    def test_office_can_only_be_created_once(self):
        amity = Amity()
        with patch('amity.rooms.room.Office'):
            amity.create_room('o', 'orange')
            result = amity.create_room('o', 'orange')
            self.assertEqual(result, 'Room already exists.')

    def test_room_creation_when_successful(self):
        amity = Amity()
        with patch('amity.rooms.room.Office'):
            result = amity.create_room('o', 'krypton')
            self.assertEqual(result, 'Room Krypton created.')
        amity = Amity()
        with patch('amity.rooms.room.LivingSpace'):
            result = amity.create_room('l', 'haskell')
            self.assertEqual(result, 'Room Haskell created.')

    # Print allocations method test begins here
    def test_returns_no_allocations_if_no_rooms_created(self):
        amity = Amity()
        self.assertEqual(amity.print_allocations(),
                         'Error. No rooms within system.')
    # add_person method testing begins here

    def test_returns_error_if_no_rooms_within_system(self):
        amity = Amity()
        result = amity.add_person('Jackie', 'Maribe', 'Fellow', 'Y')
        self.assertEqual(result, 'There are no rooms in the system.')

    def test_validation_of_people_names(self):
        amity = Amity()
        amity.create_room('o', 'lime')
        res = amity.add_person('Jackie', 45, 'Fellow', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Wrong type for name.')
        res2 = amity.add_person('J6327', 'Maribe', 'Fellow', 'Y')
        self.assertTrue(res2)
        self.assertEqual(res2, 'Non-Alphabetical names added')

    def test_validation_of_people_types(self):
        amity = Amity()
        amity.create_room('o', 'cyan')
        res = amity.add_person('alex', 'graham', 'worker', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Invalid Person Type')

    def test_staff_cannot_want_accomodation(self):
        amity = Amity()
        amity.create_room('l', 'ruby')
        res = amity.add_person('alex', 'graham', 'staff', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Staff cannot have wants accomodation of Y.')

    def test_wants_accomodation_is_either_y_or_n(self):
        amity = Amity()
        amity.create_room('o', 'lilac')
        res = amity.add_person('seralynnette', 'nduta', 'Fellow', 'Yes')
        self.assertTrue(res)
        self.assertEqual(res, 'Wants accomodation not Y or N')

    def test_validation_if_person_fellow_and_wants_accomodation(self):
        '''
        Both a living space and office must exist for a fellow who
        wants accomodation.
        '''
        amity = Amity()
        amity.create_room('o', 'pyrex')
        res = amity.add_person('wycliffe', 'wangondu', 'Fellow', 'Y')
        self.assertTrue(res)
        self.assertEqual(res, 'No Living space for fellow requiring both.')

    def test_passes_validation_and_creates_person(self):
        # Since there are only two rooms: one of each Living Space and Office
        # and person wants accomodation
        # we are sure the rooms allocated are as created.
        amity = Amity()
        amity.create_room('o', 'clandy')
        amity.create_room('l', 'calamity')
        amity.add_person('myanmar', 'wakesho', 'Fellow', 'y')
        for room in amity.rooms:
            if room.room_name == 'Clandy':
                self.assertIn('Myanmar Wakesho', room.occupants)
                self.assertEqual(len(room.occupants), 1)
            if room.room_name == 'Calamity':
                self.assertIn('Myanmar Wakesho', room.occupants)
                self.assertEqual(len(room.occupants), 1)

    def test_person_objects_are_created(self):
        amity = Amity()
        amity.create_room('o', 'mars')
        amity.create_room('l', 'earth')
        amity.add_person('justine', 'kariuki', 'Fellow', 'y')
        for person in amity.people:
            if person.full_name == 'Justine Kariuki':
                self.assertEqual(person.person_type, 'Fellow')
                self.assertEqual(person.identifier, 'F1')

        amity.add_person('alec', 'kambua', 'Staff', 'n')
        for person in amity.people:
            if person.full_name == 'Alec Kambua':
                self.assertEqual(person.person_type, 'Staff')
                self.assertEqual(person.identifier, 'S1')

    def test_get_identifier_if_no_people_added(self):
        amity = Amity()
        self.assertEqual(amity.get_identifier(
            'Lydiah', 'Kan'), 'No people added')

    def test_get_identifier_if_people_added(self):
        amity = Amity()
        amity.create_room('o', 'yellow')
        amity.create_room('l', 'blue')
        amity.add_person('brandon', 'balagu', 'Fellow', 'y')
        self.assertEqual(amity.get_identifier(
            'brandon', 'balagu'), 'F1')
    # Test Reallocate Person starts here

    def test_reallocate_person(self):
        amity = Amity()
        amity.create_room('o', 'Jupiter')
        amity.create_room('o', 'Pluto')
        amity.add_person('isaac', 'kimani', 'staff', 'n')
        res = amity.reallocate_person('S1', [])
        self.assertEqual(res, "Error. Please enter valid room name.")

    def test_reallocate_person_when_room_does_not_exist(self):
        amity = Amity()
        amity.create_room('o', 'Mars')
        amity.create_room('o', 'Venus')
        amity.add_person('Nduta', 'Nungari', 'staff', 'n')
        res = amity.reallocate_person('S1', 'Neptune')
        self.assertEqual(res, "Room does not exist.")

    def test_reallocate_person_when_person_accomodate_is_N(self):
        amity = Amity()
        amity.create_room('o', 'Mars')
        amity.create_room('l', 'Venus')
        amity.add_person('Xander', 'Akura', 'Fellow', 'n')
        res = amity.reallocate_person('F1', 'Venus')
        self.assertEqual(res, 'Fellow does not want accomodation')
        for room in amity.rooms:
            if room.room_name == 'Venus':
                self.assertNotIn('Xander Akura', room.occupants)

    def test_reallocate_to_same_room(self):
        amity = Amity()
        amity.create_room('o', 'Mars')
        amity.add_person('michelle', 'wanjiru', 'Fellow', 'n')
        res = amity.reallocate_person('F1', 'Mars')
        self.assertEqual(res, 'cant reallocate to same room')

    def test_reallocate_to_same_room_if_person_id_non_exitent(self):
        amity = Amity()
        amity.create_room('o', 'Mars')
        amity.create_room('o', 'Venus')
        amity.add_person('serallynnette', 'wanjiku', 'Staff', 'n')
        res = amity.reallocate_person('Staff1', 'Mars')
        self.assertEqual(res, 'Invalid person id.')

    def test_reallocate_person_works(self):
        amity = Amity()
        amity.create_room('o', 'valhalla')
        amity.add_person('seralynnette', 'wanjiku', 'Staff', 'n')
        amity.create_room('o', 'narnia')
        res = amity.reallocate_person('S1', 'narnia')
        self.assertEqual(res, 'Person reallocated to Narnia')
        for room in amity.rooms:
            if room.room_name == 'Valhalla':
                self.assertNotIn('Seralynnette Wanjiku', room.occupants)
            if room.room_name == 'Narnia':
                self.assertIn('Seralynnette Wanjiku', room.occupants)

    # test_print_room_works
    def test_print_room_if_no_rooms(self):
        amity = Amity()
        res = amity.print_room('Jupite')
        self.assertEqual(res, 'No rooms exist at the moment.')

    def test_if_room_exists(self):
        amity = Amity()
        amity.create_room('o', 'jupite')
        res = amity.print_room('SOHK')
        self.assertEqual(res, 'Room does not exist.')

    # test print unallocated
    def test_print_unallocated_if_all_allocated(self):
        amity = Amity()
        mocked_room = Mock()
        mocked_room.room_name = 'Lyon'
        mocked_room.room_type = 'Office'
        amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        res = amity.print_unallocated()
        self.assertEqual(res, 'No unallocated people as per now.')

    def test_print_unallocated_if_exisiting(self):
        amity = Amity()
        mocked_room = Mock()
        mocked_room.room_name = 'Witherspoon'
        mocked_room.room_type = 'Office'
        amity.add_person('Lyon', 'Witherspoon', 'Staff', 'n')
        amity.unallocated_persons.append('Person Name')
        res = amity.print_unallocated()
        self.assertEqual(res, 'Some people unallocated.')

