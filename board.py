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


	
	def apply_action(action,attack_state,grave):
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
			if not xy_under_attack in ships_under_attack or not self.one_group(ships_under_attack):
				print "INCORRECT MOVE:", action
				print "In attack state 1", xy_under_attack
				grave = self.remove_ships(ships_under_attack+[xy_under_attack], grave)
				return (0,None,None), grave
			else:
				return (2,xy_under_attack,ships_under_attack), grave

		elif att_type == 2:  # player 2 finished attack
			attacking_ships = action
			attacked_ships = XYs
			attack_state = (0,None,None)
			grave = self.battle(attacking_ships,attacked_ships, grave)
			return attack_state,grave


	def battle(self,attacking_ships,attacked_ships, grave):
		grave = remove_ships(attacking_ships, grave)
		grave = remove_ships(attacked_ships, grave)
		return grave

	def remove_ships(self,ships_list, grave):
		for i in ships_list:
			(x,y)=i
			if board[y][x] != None:
				grave[board[y][x].name()][board[y][x].color()]=grave[board[y][x].name()][board[y][x].color()]+1
				board[y][x] = None
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
			



	def show_board(self):
		n=self.n
		for i in range(n):
			a=" "*(n*3-2-i*3)
			for j in range(i):
				a=a+"__/"
				a=a+self.get_ship_name(i+1-2*n,1-i+j*2)
				a=a+"\\"
			a=a+"__"
			a=a+" "*(n*3-2-i*3)
			print a
		for i in range(n):
			a=""
			for j in range(n-1):
				a=a+"/"
				a=a+self.get_ship_name(1-n+2*i,1-n+j*2)
				a=a+"\\__"
			a=a+"/"
			a=a+self.get_ship_name(1-n+2*i,1-n+(n-1)*2)
			a=a+"\\"
			print a
			a=""
			for j in range(n-1):
				a=a+"\\__/"
				a=a+self.get_ship_name(2-n+2*i,2-n+j*2)
			a=a+"\\__/"
			print a
		for i in range(n-1):
			a=""
			a=a+"   "*(i+1)
			for j in range(n-2-i):
				a=a+"\\__/"
				a=a+self.get_ship_name(n+1+i,3-n+i+j*2)
			a=a+"\\__/"
			a=a+"   "*(i+1)
			print a



	def get_ship_name(self,x,y):
		if self.board[y][x] == None:
			return"  "
		else:
			return self.board[y][x].short_name()

	

	def ship_move(self,old_xy,nex_xy):
		(x,y)=nex_xy
		if self.board[y][x]!=None:
			raise "Eror can not do this move"
		(ox,oy)=old_xy
		self.board[y][x]=self.board[oy][ox]
		self.board[oy][ox]=None
		pass



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

