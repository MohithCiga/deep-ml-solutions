import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	"""Write your code here and return a python list after reshaping by using numpy's tolist()"""
  
	try:
		reshaped_matrix = np.reshape(a,new_shape)
	except:
		reshaped_matrix = np.array([]) #return empty list if reshaping is not possible and an error is thrown

	reshaped_matrix = reshaped_matrix.tolist()

	return reshaped_matrix
