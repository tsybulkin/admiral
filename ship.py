#
#

from state import ships_state


class Ship():
	def __init__(self,color,name,ID):
		self.color = color
		if name in ships_state:
			self.name = name
		else:
			print '** There is no ship with the name:',name, '**\n'
			raise
		self.id = ID
		self.detected = False
		self.under_attack = False
		

	
	def short_name(self):
		if self.name=='Cruiser': a='Cr'
		elif self.name=='Esminets': a='Es'
		elif self.name=='Torpedo boat': a='TB'
		elif self.name=='Tral': a='Tr'
		elif self.name=='Submarine': a='Sb'
		elif self.name=='Base': a='Bs'
		elif self.name=='Nuclear bomb': a='NB'
		elif self.name=='Mine': a='Mn'
		elif self.name=='Torpedo': a='To'
		else:
			raise "wrong ship name"
		if self.color=="black":
			return ("\033[91m{}\033[00m" .format(a))
		else:
			return ("\033[92m{}\033[00m" .format(a))

