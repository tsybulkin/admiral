




def check_connectivity(XYs):
	if len(XYs) <= 1: return True

	first, rest = XYs[0], XYs[1:]
	done = []
	inwork = [first]

	while len(inwork)*len(rest)!=0:
		element = inwork.pop(0)
		neig = get_neighbors(element)
		i = 0
		while len(rest)>i:
			if rest[i] in neig:
				inwork.append(rest.pop(i))
			else:
				i=i+1
	if len(rest) == 0: return True
	else: return False


def get_neighbors(XY,n):
	x,y = XY
	#if not cor_cord(x,y,n): raise "incorrect cord"
	res = []
	preres = [(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1),(x-2,y),(x+2,y)]
	for (x,y) in preres:
		if cor_cord(x,y,n): res.append((x,y))
	return res

def cor_cord(x,y,n):
	if abs(y)>=n: return False
	elif abs(x)>n*2-2: return False
	elif (x+y)%2 != 0: return False
	elif abs(x)+abs(y)>n*2-2: return False
	else: return True

