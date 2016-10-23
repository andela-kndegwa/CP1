import unittest
from room import LivingSpace, Office


class TestRoomClassFunctionality(unittest.TestCase):
    """docstring for TestRoomClassFunctionality
    This Class Checks to make sure the objects created are indeed
    instances of the classes that they are instantiated from.
    It also mocks some of the methods and ensures they return
    values as expected.
        """

    def test_office_is_instance_of_class_Office(self):
        '''
        This simply tests that the room type and room_name are passed
        accordingly for a office. The second assert tests whether string
        formatting actually occurred
        '''
        office = Office('valhalla')
        self.assertEqual('Office', office.room_type)
        self.assertNotEqual('valhalla', office.room_name)

    def test_living_space_is_instance_of_class_LivingSpace(self):
        ls = LivingSpace('Python')
        self.assertEqual('Living Space', ls.room_type)

    def test_capacity_of_objects(self):
        """
        The capacity of an office is set to 6
        and that of a living space is set to 4.
        This assert confirms that.
        """
        office = Office('oculus')
        ls = LivingSpace('ruby')
        self.assertEqual(office.capacity, 6)
        self.assertEqual(ls.capacity, 4)

    def test_capacity_reduces_by_one_for_living_space(self):
        '''
        The mock method here abstracts the room occupants indeed do
        decrease by one when the add person function is called.
        '''
        ls = LivingSpace('haskel')
        self.assertEqual(ls.add_person('one'), 3)

    def test_capacity_reduces_by_one_for_office(self):
        '''
        The mock method here abstracts the room occupants indeed do
        decrease by one when the add person function is called.
        '''
        of = Office('narnia')
        self.assertEqual(of.add_person('one'), 5)
