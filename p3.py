
#  Program # 3
#  Matrix multiplication in python 3
#  CS320
#  10/14/2019
#  @author  Jacob Byerline cssc0457
#

import sys
# This function begins execution of program.
# Verify data input filename provided on command line: len(sys.argv)
# If error, output message for user: Usage: p3.py dataFileName'
# and quit, using sys.exit()
#
# Declare A, B, call read_matrices to initialize A, B, and store
# return value as C
#
# Print A and B contents
#
# Call mult_matrices
#
# Print result contents
#
def main():

    for i in sys.argv:
        print(i)


    if(len(sys.argv) == 2 or len(sys.argv) == 0):
        matA = []
        matB = []
        matC = read_matrices(matA, matB)
        print("Program #3, cssc0457, Jacob Byerline")
        print("Matrix A conents:")
        for x in matA:
            print(*x, sep = '\t')
        print()
        print("Matrix B conents:")
        for x in matB:
            print(*x, sep = '\t')
        print()
        mult_matrices(matA, matB, matC)
        print_matrix(matC)
    else:
        print("usage: p3.py dataFileName")
        print('Number of arguments:'), len(sys.argv), ('arguments.')
        print('Argument List:', str(sys.argv))
        sys.exit()

# This function reads m, n, and p from the datafile.
# Then matrices A and B are filled from the datafile.
# Matrix C is then allocated size m x p.
# The values for m, n, and p are local values filled in by this function
# PARAMETERS in order are:
# list matrix A
# list matrix B
# RETURN matrix C
#
def read_matrices(A,B):

    count = 0
    m = 0
    n = 0
    p = 0
    matA = A
    matB = B
    filename = sys.argv[1]
    
    with open(filename) as f:
         for item in f:
                count += 1
                if count == 1:
                    m = int(item)
                elif count == 2:
                    n = int(item)
                elif count == 3:
                    p = int(item)
                elif count > 3 and count <= 3 + m:
                    item = item.replace('\n', '')
                    num = 1
                    for i  in range(num):
                        row = item.split()
                        for i in range(len(row)):
                            row[i] = int(row[i])
                        matA.append(row)
                elif count >= 4 + m and count <= 4 + m + n:
                    item = item.replace('\n', '')
                    num = 1
                    for i  in range(num):
                        row = item.split()
                        for i in range(len(row)):
                            row[i] = int(row[i])
                        matB.append(row)
           
    matC = [[0 for x in range(p)] for y in range(m)] 

    return matC


# This function prints a matrix. Rows and columns should be preserved.
# PARAMETERS in order are:
# list The matrix to print
#
def print_matrix(matrix):

    print("Matrix A * B is:")
    for x in matrix:
        print(*x, sep = "\t")


# The two matrices A and B are multiplied, and matrix C contains the
# result.
# PARAMETERS in order are:
# list Matrix A
# list Matrix B
# list Matrix C (all zeros at this point)
#
def mult_matrices(A,B,C):

    for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]

if __name__ == '__main__':
    main()