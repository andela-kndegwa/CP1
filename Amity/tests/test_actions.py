import unittest
from ..actions import *

class TestActionsAmity(unittest.TestCase):
    def test_creates_a_single_room(self):
        create_room('O', 'Krypton')
        # last room is Krypton check
        self.assertIsNotNone(rooms)

    def test_returns_valid_type_living_space(self):
        create_room('l', 'Krypton')
        self.assertIn('Krypton', rooms['livingSpaces'])

    def test_returns_valid_type_office(self):
        create_room('o', 'Uber')
        self.assertIn('Uber', rooms['offices'])

    def test_returns_msg_when_room_doesnt_exist(self):
        self.assertEqual(get_room_type('Narnia'),
                         'The room does not exist in our system')

    def test_can_create_multiple_rooms(self):
        create_room('o', 'Kamu', 'Kaba', 'NY')
        self.assertEqual(len(rooms['offices']), 3)

    def test_returns_error_when_user_exists(self):
        add_person('Jamleck', 'Opondo', 'S')
        self.assertEquals(add_person(
            'Jamleck', 'Opondo', 'S'), 'Already exists!')

    def test_rooms_increase_by_one_on_creation(self):
        before = len(rooms['offices'])
        create_room('O', 'Java')
        after = len(rooms['offices'])
        self.assertGreater(after, before)

    unittest.skip('To test the print allocations works ')

    def test_print_allocations(self):
        pass

    unittest.skip(
        'To test also that the print unallocated function also works')

    def test_print_unallocated(self):
        pass
