#
#

from state import ships_state


class Ship():
	def __init__(self,color,name,ID):
		self.color = color
		if name in ships:
			self.name = name
		else:
			print '** There is no ship with the name:',name, '**\n'
			raise
		self.id = ID
		self.detected = False
		self.under_attack = False
		

	def set_coords(self,x,y):
		self.x = x
		self.y = y




