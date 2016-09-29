import sys
import os
from models import Fellow, Staff, Office, LivingSpace
from database import session
from Rooms.living_space import LivingSpace
from Rooms.office import Office
from People.fellow import Fellow
from People.staff import Staff

class Amity(object):
	def __init__(self):
		pass
	def create_room(self, room_name, rom_type):
		if self.room_type is 'O':
			office = Office.create_room()
