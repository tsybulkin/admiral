class Board():
	def __init__(self,n):
		cell_list=[]
		for i in range(n):
			cell_list.append((None,)*(n*4-3-i*2))
		for i in range(n):
			cell_list.append((None,)*((n+i)*2-1))
		self.n=n
		self.board=tuple(cell_list)

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
		pass
		

	def ship_move(self,old_xy,nex_xy):
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


	def free_sea_level(self):
		if self.n<7: return 1
		else: return int(n/3)