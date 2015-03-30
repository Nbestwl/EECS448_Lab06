import csv

#open and read in the csv file
def file2mat(filename):
    file = open(filename,'rU')
    filecsv = csv.reader(file)
    mat = []
    for row in filecsv:
        mat.append([int(x) for x in row ])
    file.close()
    return mat

#check if the csv file is actually metrices
def check(matrix):
    ismatrix = True
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            ismatrix = False
    if ismatrix == False:
        print ('Not the same length')
        return 0
    else:
        print ('It is a matrix')
        return 1

#matrix addition
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

#matrix transpose
def mattrans(mat1):
    h = len(mat1)
    w = len(mat1[0])
    mat2 = [[mat1[row][col] for row in range(0, h)] for col in range(0, w)]
    return mat2

#do the matrix multiplication
def mult(matrix1,matrix2):
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[0])
    if col1 == row2:
        #do the muilplication here
        newMatrix = [[0 for x in range(0,col2)] for y in range(0,row1)]
        for row in range(0,row1):
            for col in range(0,col2):
                for k in range(0,col1):
                    #print(str(row) + ", " + str(col) + " -- k=" + str(k))
                    newMatrix[row][col] += matrix1[row][k] * matrix2[k][col]
    else:
        print ('Matrix size does not match for multiplication')
    return newMatrix

file1 = 'Matrice1.csv'
file2 = 'Matrice2.csv'
file3 = 'Matrice3.csv'
file4 = 'Matrice4.csv'
mat1 = file2mat(file1)
mat2 = file2mat(file2)
mat3 = file2mat(file3)
mat4 = file2mat(file4)
print (mat1)
print (mat2)
print (mat3)
print (mat4)
#if the matrices for multiplication are not matrices, then exit the program
if check(mat1) == 0 or check(mat2) == 0:
    quit()
    
check(mat3)
check(mat4)
print (mult(mat1,mat2))
print (matadd(mat3,mat4))
print (mattrans(mat1))
