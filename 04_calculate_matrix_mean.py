def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []
	if mode == "column":
		for j in range(len(matrix[0])):
			sum = 0
			for i in range(len(matrix)):
				sum += matrix[i][j]
			means.append(sum/len(matrix))
	
	elif mode == "row":
		for j in range(len(matrix)):
			sum = 0
			for i in range(len(matrix[0])):
				sum += matrix[j][i]
			means.append(sum/len(matrix[0]))	

	else:
		print("Invalid mode!!!")	


	return means
