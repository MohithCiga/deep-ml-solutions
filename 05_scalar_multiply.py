def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	rows = len(matrix)
	cols = len(matrix[0])

	result = [[-1] * rows for i in range(cols)] 

	for i in range(rows):
		for j in range(cols):
			result[i][j] = matrix[i][j] * scalar

	return result
