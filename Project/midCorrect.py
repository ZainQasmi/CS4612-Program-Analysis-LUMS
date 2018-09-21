def mid(x,y,z):
	m = z
	if (y<z):
		if(x<y):
			m = y
		elif (x<z):
			m = x          #bug
	else:
		if(x>y):
			m = y
		elif (x>z):
			m = x

	#print "Middle Number is: " + str(m)
	return m
