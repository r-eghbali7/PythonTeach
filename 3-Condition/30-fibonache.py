def fibDirect(n):
	a = 1
	b = 1
	temp = 0

	for x in range(2,n):
		temp = b
		b = a + b
		a = temp

	return (b)

fibDirect(8)
