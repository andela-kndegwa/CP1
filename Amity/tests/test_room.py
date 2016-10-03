import unittest  # A common Python testing framework
from os import sys, path
from ..Rooms.room import Room
from ..Rooms.living_space import LivingSpace
from ..Rooms.office import OfficeSpace

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

"""
Also makes a relative import to get the Room, Living Space
and Office classes just created for the purpose of testing
"""


class TestRoomFunctionality(unittest.TestCase):
    """
    This class is intended to test the Functionality of The Room
    class as modelled together with its subclasses LivingSpace &
    Office.
    """

    def test_created_room_is_instance(self):
        '''
        Room1 needs to be an instance of Room class.
        The Room class has been modelled as having
        to first accept no arguments but then later
        the create_room function states the room name
        and room type.
        '''
        room1 = Room()
        self.assertIsInstance(room1, Room)

    def test_created_room_takes_name(self):
        '''
        The rooms have to take the exact name specified
        in the string. Thus ANY OTHER case should fail.

        '''
        room2 = Room()
        room2.create_room('Clojure', 'O')
        self.assertEqual(room2.room_name, 'Clojure')
        self.assertNotEqual(room2.room_name, 'CLOJURE')
        self.assertNotEqual(room2.room_name, 'cLOJuRE')

    def test_rooms_names_are_strings_only(self):
        room3 = Room()
        room3.create_room('Oculus', 'L')
        self.assertTrue(type(room3.room_name), str)

    def test_room_capacity(self):
        room4 = LivingSpace()
        room4.create_room('TestLivingSpace', 'O')
        self.assertEquals(room4.roomCapacity, 4)
        room5 = OfficeSpace()
        room5.create_room('TestOffice', 'L')
        self.assertEquals(room5.roomCapacity, 6)

    def test_new_room_is_initially_empty(self):
        r6 = OfficeSpace()
        r6.create_room('A', 'L')
        self.assertIs(type(r6.occupants), list)
        self.assertEqual(len(r6.occupants), 0)
