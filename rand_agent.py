#
# rabdom agent
#
from sunk_ships import ships_state
from ship import Ship
import random
from tools import get_neighbors




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
		(color, attack_state, board, grave) = state
		(att_type, xy_under_attack, XYs) = attack_state
		
		if att_type == 0:  # NO_ATTACK
			movable_ships = get_movable_ships(board, color)
			ship_xy = random.choice(movable_ships)
			new_cell = get_empty_cell(ship_xy, board)
			board_after_move = board.copy()
			board_after_move.ship_move(ship_xy, new_cell)
			enemies = []
			enemies = get_enemies_in_contact(board_after_move, color)
			enemies.append(None)
			return ( (ship_xy,new_cell), random.choice(enemies) )


		elif att_type == 1:
			return [xy_under_attack]


		elif att_type == 2:
			
			attacking_ships = get_my_ships_close_to(xy_under_attack, board, color)
			return [ random.choice(attacking_ships) ]


		else: raise



def get_my_ships_close_to(xy, board, color):
	neib = get_neighbors(xy, board.n)
	res = []
	for (x,y) in neib:
		if board.board[y][x] == None: continue
		if board.board[y][x].color == color:
			res.append((x,y))
	return res




def get_movable_ships(board, color):
	res = []
	n = board.n
	for y in range(1-n,n):
		for x in range(-(n-1)*2,2*n-1):
			if board.board[y][x] != None:
				if board.board[y][x].color == color:
					neib = get_neighbors((x,y),n)
					for (nx,ny) in neib:
						if board.board[ny][nx] == None:
							res.append((x,y))
							break
	return res




def get_enemies_in_contact(board, color):
	res = []
	n = board.n
	for y in range(1-n,n):
		for x in range(-(n-1)*2,2*n-1):
			if board.board[y][x] != None:
				if board.board[y][x].color != color:
					neib = get_neighbors((x,y),n)
					for (nx,ny) in neib:
						if board.board[ny][nx] == None: continue 
						if board.board[ny][nx].color == color:
							res.append((x,y))
							break
	return res





def get_empty_cell(ship_xy, board):
	(x,y) = ship_xy
	neib = get_neighbors((x,y),board.n)
	res = []
	for (x,y) in neib:
		if board.board[y][x] == None:
			res.append((x,y))
	if len(res)==0:
		return None
	return random.choice(res)