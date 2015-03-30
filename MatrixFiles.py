#These should work as the matrix addition function and the matrix transposing function.
#- Harrison

#I'm pretty confindent on the addition function but I'm not 100%. It might need work.
def matadd(mat1, mat2)
	if len(mat1) != len(mat2) || len(mat1[0]) != len(mat2[0])
		print "The matrices are not able to be added."
	else
		c = len(mat1)
		r = len(mat1[0])
		matC[[r]c]
		for x in xrange(0, len(mat1)):
			for y in xrange(0, len(mat1[0])):
				matC[[x]y] = mat1[[x]y] + mat2[[x]y]
				print matC
				

#This is the transposing function. Should work. Returns the transposed matrix.
def mattrans(mat1)
	h = len(mat1)
	w = len(mat1[0])
	mat2 = [[mat1[row][col] for row in range(0, h)] for col in range(0, w)]
	return mat2