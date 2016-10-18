import mock
import unittest

from amity import Amity


class TestAmity(unittest.TestCase):
    def test_reallocate_person(self):
        amity = Amity()
        cyan = mock.MagicMock()
        hogwarts = mock.MagicMock()
        hogwarts.occupants = ["kimani"]
        hogwarts.room_name = "hogwarts"
        kimani = mock.MagicMock()
        kimani.identifier = "F1"
        kimani.full_name = "kimani"
        njira = mock.MagicMock()
        njira.identifier = "F2"
        njira.full_name = "njira"
        amity.offices = {'available': [cyan, hogwarts]}
        amity.people = [kimani, njira]
        response = amity.reallocate_person('F1', "Cyan")
        self.assertEqual(response, "F1 has been reallocated to Cyan")


