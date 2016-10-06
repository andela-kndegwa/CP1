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

    def test_if_fellow_wants_accomodation(self):
        f = Fellow()
        f.person_name = 'Kimani'
        f.wants_accomodation = 'y'
        self.assertEquals(f.check_wants_accomodation(), 'Wants accomodation')

    def test_last_response_invalid(self):
        f2 = Fellow()
        f2.person_name = 'Wanja'
        f2.wants_accomodation = 'sajkjak'
        self.assertEqual(f2.check_wants_accomodation(),
                         'Last response invalid')
