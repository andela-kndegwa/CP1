import unittest
from ..People.person import Person
from ..People.staff import Staff
from ..People.fellow import Fellow


class TestPersonFunctionality(unittest.TestCase):
    def test_person_is_instance(self):
        person = Person()
        self.assertIsInstance(person, Person,
                              msg="person must be an instance of Person")

    def test_add_person_name_works(self):
        p = Person()
        p.person_name = 'Kamau'
        self.assertEqual(p.person_name, 'Kamau')

    def test_fellow_and_staff_different(self):
        s = Staff()
        f = Fellow()
        self.assertNotEqual(s, f)

    def test_fellow_is_right_instance(self):
        fellow = Fellow()
        self.assertIsInstance(fellow, Fellow)

    def test_staff_is_right_instance(self):
        staff = Staff()
        self.assertIsInstance(staff, Staff)
