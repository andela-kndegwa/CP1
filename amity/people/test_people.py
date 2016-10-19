import unittest
from person import Staff, Fellow


class TestPersonClassFunctionality(unittest.TestCase):
    '''
    This class is effectively used to manage the basics
    of how the Person class passes its properties to
    Fellow and Staff and handles how they are managed.
    '''

    def test_staff_person_type(self):
        s = Staff('alex', 'mahugu')
        self.assertEqual(s.person_type, 'Staff')
        # string formatting should occur as highlited above

    def test_fellow_person_type(self):
        s = Fellow('alison', 'muraya')
        self.assertEqual(s.person_type, 'Fellow')
        # string formatting should occur as highlited above
