




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


def get_neighbors(XY):
	X,Y = XY
	return [(X+2,Y),(X-2,Y),(X+1,Y+1),(X+1,Y-1),(X-1,Y+1),(X-1,Y-1)]
