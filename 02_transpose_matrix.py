def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	rows = len(a) 
	cols = len(a[0]) 

	answer = []

	for c in range(cols):
		sub_array = []
    
		'''collect 1st elements of each row then 2nd elements in next iteration etc...'''
		for r in range(rows):
			sub_array.append(a[r][c])
      
		'''Append transposed sub arrays into our answer list'''
		answer.append(sub_array)

	return answer
