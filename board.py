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
		if y>self.n/3-1: return "BL"
		if y<-self.n/3+1: return "WL"
		else: return "  "
		return str(abs(x)%10)+str(abs(y)%10)

	def ship_move(self,old_xy,nex_xy):
		pass