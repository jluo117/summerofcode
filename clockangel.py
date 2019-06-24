def converttopair(T): 
	if T<= 3 && T >0:
		return(T,3,T)
	if T < 6 && T >= 4:
		x = 6 - T
		return (x,-(3-x))
	if T <= 9 && T >= 7:
		x = T - 6
		return (-x, - (3 -x))
	else:
		x = 12 - T
		return (-x ,3 -x)

def angelCov(h,m):
	if h > 12:
		h = h -12
	h = h + m/60
	m = m/60 * 12
	hCord = converttopair(h)
	mCord = converttopair(m)
	angelBetween = np.angel(h,m) #assuming that there is an np function that finds distance btw two lines
	if angelBetween > 180:
		return (360 - angelBetween)
	else:
		return angelBetween
def totaltick():
	total = 0
	for i in range(1,25):
		for j in range(1,61):
			if angelCov(i,j) == 0:
				total += 1
	return total
