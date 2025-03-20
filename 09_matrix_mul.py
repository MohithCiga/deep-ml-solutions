def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0])!=len(b):
		return -1
	
	row1, col1 = len(a), len(a[0])
	row2, col2 = len(b), len(b[0])

	c = [[0 for i in range(col2)] for _ in range(row1)]

	for i in range(row1):
		for j in range(col2):
			for k in range(col1):
				c[i][j] += a[i][k]*b[k][j]


	return c