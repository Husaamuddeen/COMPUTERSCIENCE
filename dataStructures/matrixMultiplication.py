'''2d Array: Matrix Multiplication
⭐⭐

Challenge: 
Write a function that takes two 2D arrays as input and returns their matrix multiplication'''



def matrixMultiplication(matrix1, matrix2):
    newMatrix = [
        [None, None],
        [None, None]
    ]
    newMatrix[0][0] = matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0]
    newMatrix[0][1] = matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]
    newMatrix[1][0] = matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0]
    newMatrix[1][1] = matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1]

    return newMatrix

matrix1 = [
    [5,7],
    [3,4]
]

matrix2 = [
    [2,7],
    [1,6]
]

print(matrixMultiplication(matrix1,matrix2))