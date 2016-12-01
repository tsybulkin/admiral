#
# rabdom agent
#
from sunk_ships import ships_state
from ship import Ship
import random




class RandomAgent():
	def __init__(self,color):
		assert(color == 'black' or color == 'white')
		self.color = color


	def set_ships(self, fields):
		ships = []
		remaining_ships = []
		for name in ships_state.keys():
			for i in range(ships_state[name]['total']):
				ship = Ship(self.color, name, i)
				j = random.randint(0,len(fields)-1)
				remaining_ships.append( (fields.pop(j),ship) )

		return remaining_ships


	def get_action(self, state):
		(color,attack_state,board,grave) = state
		(att_type, xy_under_attack, XYs) = attack_state
		own_ships, enemies = board.get_ships(color)

		if att_type == 0:  # NO_ATTACK
			random.choice()


		elif att_type == 1:


		elif att_type == 2:


		else: raise


