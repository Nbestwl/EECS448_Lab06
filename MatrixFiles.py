#These should work as the matrix addition function and the matrix transposing function.
#- Harrison

#I'm pretty confindent on the addition function but I'm not 100%. It might need work.
def matadd(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print ('The matrices are not able to be added.')
    else:
        row = len(mat1)
        col = len(mat1[0])
        mat3 = [[0 for x in range(0,col)] for y in range(0,row)]
        for i in range(0,row):
            for j in range(0,col):
                mat3[i][j] = mat1[i][j] + mat2[i][j]
        return mat3	
				

#This is the transposing function. Should work. Returns the transposed matrix.
def mattrans(mat1)
	h = len(mat1)
	w = len(mat1[0])
	mat2 = [[mat1[row][col] for row in range(0, h)] for col in range(0, w)]
	return mat2
