import unittest  # A common Python testing framework
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
        room2.create_room('Clojure', 'Living Space')
        self.assertEqual(room2.room_name, 'Clojure')
        self.assertNotEqual(room2.room_name, 'CLOJURE')
        self.assertNotEqual(room2.room_name, 'cLOJuRE')

    def test_rooms_names_are_strings_only(self):
        room3 = Room()
        room3.create_room('Oculus', 'Office')
        self.assertTrue(type(room3.room_name), str)


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from Rooms.room import Room, LivingSpace, Office
        unittest.main()
    else:
        from ..Rooms.room import Room, LivingSpace, Office
