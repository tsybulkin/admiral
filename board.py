#
#Class Board
#
import tools



class Board():

	def __init__(self,n):
		cell_list=[]
		for i in range(n):
			cell_list.append([None]*(n*4-3-i*2))
		for i in range(n):
			cell_list.append([None]*((n+i)*2-1))
		self.n=n
		self.board=cell_list


	def terminate(self, color,grave):
		for j in range(len(self.board)):
			for i in range(len(board[j])):
				if self.board[j][i].color == color and self.board[j][i].name == 'Base':
					self.board[j][i] = None
		grave['Base'][color] = grave['Base']['Total']


	def copy(self):
		n = self.n
		board_copy = Board(n)
		board_copy.board = [a[:] for a in self.board[:]]
		return board_copy



	def action_illegal(self, attack_state, action): 
		att_type,xy_under_attack,XYs = attack_state
		if att_type == 0:
			# check that action is a tuple (Move, Field)
			# Move = (old_field, new_field)
			(move, attack_field) = action
			if move != None:
				(x_o,y_o), (x_n,y_n) = move
				if not tools.cor_cord(x_o,y_o,self.n): 
					print "illegal coordinates:", x_o,y_o
					return True
				if not tools.cor_cord(x_n,y_n,self.n): 
					print "illegal coordinates:", x_n,y_n
					return True
				if self.board[y_n][x_n] != None: 
					print "illegal move into non-empty cell"
					return True

		elif att_type == 1:
			# check that action is a non-empty list of max 3 elements
			# all elements should contain neighboring fields with the same ships
			pass
		else:
			# check that action is a non-empty list of max 3 elements
			# all elements should contain neighboring fields with the same ships

			pass

		return False


	
	def apply_action(self,action,attack_state,grave):
		(att_type,xy_under_attack,XYs) = attack_state

		if att_type == 0:  # NO_ATTACK
			(move, field) = action
			if move != None: 
				(oxy, nxy)=move
				self.ship_move(oxy,nxy)
			if field != None:
				attack_state = (1,field,None)
			else:
				attack_state = (0, None,None)
			return attack_state,grave


		elif att_type == 1:  # player was attacked
			ships_under_attack = action
			return (2,xy_under_attack,ships_under_attack), grave

		elif att_type == 2:  # player 2 finished attack
			attacking_ships = action
			attacked_ships = XYs
			attack_state = (0,None,None)
			grave = self.battle(attacking_ships, attacked_ships, grave)
			return attack_state,grave


	def battle(self,attacking_ships,attacked_ships, grave):
		(xa,ya)=attacking_ships[0]
		(xd,yd)=attacked_ships[0]
		ship_a = self.board[ya][xa].name
		ship_d = self.board[yd][xd].name
		ship_ranks = ['Cruiser','Esminets','Torpedo boat','Tral','Submarine']
		ship_strength = [11., 6.8, 4.2, 2.6, 1.6, 1.]

		if ship_a == 'Base': return self.remove_ships(attacking_ships, grave)
		elif ship_a == 'Nuclear bomb': return self.nuclear_blust(attacking_ships, grave)
		elif ship_a == 'Mine': return self.remove_ships(attacking_ships, grave)
		elif ship_a == 'Torpedo': return self.remove_ships(attacking_ships, grave)
		
		elif ship_d == 'Base': return self.remove_ships(attacked_ships, grave)
		elif ship_d == 'Nuclear bomb': return self.nuclear_blust((xd,yd),grave)
		elif ship_d == 'Mine': return self.remove_ships(attacking_ships+[(xd,yd)], grave)
		elif ship_d == 'Torpedo': return self.remove_ships([(xd,yd)], grave)
		
		else: 
			print "ships:", ship_a, ship_d
			rank_a = ship_ranks.index(ship_a)
			rank_d = ship_ranks.index(ship_d)

			if abs(rank_a - rank_d) == 4: # cruiser against submarine
				if rank_a == 0: rank_a = 5
				else: rank_d == 5

			strength_a = ship_strength[rank_a]*len(attacking_ships)
			strength_d = ship_strength[rank_d]*len(attacked_ships)

			if strength_a > strength_d: return self.remove_ships(attacked_ships, grave)
			elif strength_a < strength_d: return self.remove_ships(attacking_ships, grave)
			else: return self.remove_ships(attacking_ships+attacked_ships, grave)


	def nuclear_blust (self, (xd,yd), grave ):
		#x = xd
		y = yd
		ships_list = [(x,y),(x+4,y),(x+2,y),(x-2,y),(x-4,y),(3+x,1+y),(1+x,1+y),(x-1,y+1),(x-3,y+1),(3+x-3,1-y),(1+x,1-y),(x-1,y-1),(x-3,y-1),(2+x,2+y),(x,2+y),(x-2,y+2),(2+x,2-y),(x,2-y),(x-2,y-2)]
		#for (x,y) in ships_list:
		#	if self.board[y][x] != None:
		#		if self.board[y][x].name == 'Nuclear bomb':
		#			self.nuclear_blust((x,y),grave)
		#		else: grave = self.remove_ships([(xd,yd)], grave) 
		return self.remove_ships(ships_list, grave)


	def remove_ships(self,ships_list, grave):
		for i in ships_list:
			(x,y)=i
			if self.board[y][x] != None:
				grave[self.board[y][x].name][self.board[y][x].color]=grave[self.board[y][x].name][self.board[y][x].color]+1
				self.board[y][x] = None
		return grave



	def one_group(self,ships_list):
		if len(ships_list)>3: return False
		elif len(ships_list)==1: return True
		elif len(ships_list)==0: return False
		else: 
			if tools.check_connectivity(ships_list):
				(x,y)=ships_list[0]
				ship_name = board[y][x].name()
				for i in ships_list:
					(x,y)=i
					if ship_name != board[y][x].name():
						return False

				return True

			else: return False
			

	def nstring(self,n=" ",lengs=4):
		a = str(n)
		if len(a)<lengs:
			a = a + " "
		while len(a)<lengs:
			a = " "+a
		return ("\033[44m{}\033[0m" .format(a))


	def show_board(self):
		n=self.n
		a = self.nstring(" ",5)
		for i in range(1-n,n):
			a = a + self.nstring(i,3)
		a = a + self.nstring(" ",4)
		print a
		for i in range(n):
			a=self.nstring(1-2*n+i)+" "*(n*3-2-i*3)

			for j in range(i):
				a=a+"__/"
				a=a+self.get_ship_name(i+1-2*n,1-i+j*2)
				a=a+"\\"
			a=a+"__"
			a=a+" "*(n*3-2-i*3)+self.nstring(1-2*n+i)
			print a
		for i in range(n):
			a=self.nstring(1-n+i*2)
			for j in range(n-1):
				a=a+"/"
				a=a+self.get_ship_name(1-n+2*i,1-n+j*2)
				a=a+"\\__"
			a=a+"/"
			a=a+self.get_ship_name(1-n+2*i,1-n+(n-1)*2)
			a=a+"\\"+self.nstring(1-n+i*2)
			print a
			a=self.nstring(2-n+i*2)
			for j in range(n-1):
				a=a+"\\__/"
				a=a+self.get_ship_name(2-n+2*i,2-n+j*2)
			a=a+"\\__/"+self.nstring(2-n+i*2)
			print a
		for i in range(n-1):
			a=self.nstring(n+1+i)
			a=a+"   "*(i+1)
			for j in range(n-2-i):
				a=a+"\\__/"
				a=a+self.get_ship_name(n+1+i,3-n+i+j*2)
			a=a+"\\__/"
			a=a+"   "*(i+1)+self.nstring(n+1+i)
			print a
		a = self.nstring(" ",5)
		for i in range(1-n,n):
			a = a + self.nstring(i,3)
		a = a + self.nstring(" ",4)
		print a


	def get_ship_name(self,x,y):
		if self.board[y][x] == None:
			return"  "
		else:
			return self.board[y][x].short_name()

	



	def ship_move(self,old_xy,new_xy):
		(x,y)=new_xy
		if self.board[y][x]!=None:
			raise "Error can not do this move"
		(ox,oy)=old_xy
		self.board[y][x]=self.board[oy][ox]
		self.board[oy][ox]=None

	def print_ships(self):
		for y in range(1-self.n,self.n):
			for x in range(-(self.n-1)*2,2*self.n-1):
				if self.board[y][x] != None:
					print self.get_ship_name(x,y)

	def get_initial_ship_list(self, color):
		initial_ship_list=[]
		end_line = self.free_sea_level()
		n = self.n
		y=n-1
		while y>end_line:
			x=-2*(n-1)+y
			while x<(n-1)*2-y+1:
				initial_ship_list.append((x,y))
				x=x+2
			y=y-1
		if color=='white':
			initial_ship_list = [(i,-j) for (i,j) in initial_ship_list]
		return initial_ship_list

	
	def fill_start_ships(self,list):
		for ((x,y),ship) in list:
			self.board[y][x] = ship




	def free_sea_level(self):
		if self.n<7: return 1
		else: return int(n/3)

