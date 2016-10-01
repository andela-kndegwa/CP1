import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Rooms.room import LivingSpace, Office


class Amity(object):
    """
    The Amity class is intended to be th main class in this project.
    It calls all the other classes and consolidates their information
    in one place where all the information can be drawn from.
    The CLI application thus calls Amity because it is the gateway
    to the whole application
    """

    def __init__(self):
        pass

    def get_all_staff(self):
        pass

    def get_all_fellows(self):
        pass

    def get_all_offices(self):
        pass

    def get_all_living_spaces(self):
        pass
