import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.array(T)
	S = np.array(S)
	A = np.array(A)

	if np.linalg.det(T)==0 or np.linalg.det(S)==0:
		return -1

	transformed_matrix = np.dot(np.dot(np.linalg.inv(T),A),S).tolist()
	return transformed_matrix
