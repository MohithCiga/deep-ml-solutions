def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	
	determinant = matrix[0][0]*matrix[1][1] - matrix[0][1] * matrix[1][0]
	
	inverse = ([ [matrix[1][1], -1*matrix[0][1] ],
			   [-1*matrix[1][0], matrix[0][0]]  ]) 
				
	inverse = [[i/ (determinant) for i in inverse[0]],
			   [i/ (determinant) for i in inverse[1]]]
	return inverse
