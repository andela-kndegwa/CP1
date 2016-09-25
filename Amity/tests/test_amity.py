import unittest  # Pythons main testing framework


class TestsAmityFunctionality(unittest.TestCase):
    def tests_amity(self):
        pass


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from main.amity import Amity
        unittest.main()
    else:
        from ..main.amity import Amity
