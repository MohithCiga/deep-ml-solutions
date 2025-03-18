def get_trace(matrix):
	trace = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i==j:
				trace += matrix[i][j]
	return trace

def determinant(a):
	if len(a) == 1:
		pro = a[0]
		return pro
	elif len(a) == 2:
			pro = a[0][0]*a[1][1] - a[1][0]*a[0][1]
			return pro
	else:
		pro = 0
		for i in range(len(a[0])):
			pro += ((-1)**i)*a[0][i]*determinant(new_matrix(a,i))    
		return pro  

def quadratic_formula(a, b, c):
	discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    else:
         real_part = -b / (2*a)
         imaginary_part = (abs(discriminant)**0.5) / (2*a)
         root1 = f"{real_part} + {imaginary_part}i"
         root2 = f"{real_part} - {imaginary_part}i"
         return root1, root2

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	r1, r2 = quadratic_formula(1, -get_trace(matrix), determinant(matrix))
	eigenvalues = sorted([r1,r2],reverse=True)
	
	return eigenvalues
