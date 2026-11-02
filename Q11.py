import numpy as np

#  Define Matrix A
A = np.array([[1,2],
              [5,1]
    ])

#display 
print("\nMatrix A")
print(A)

#Determinant of A

print("\nDeterminant of A :")
print(np.linalg.det(A))

#Rank of Matrix
rank = np.linalg.matrix_rank(A)
print("\nRank of a matrix A:")
print(rank)

# Inverse of Matrix
inverse = np.linalg.inv(A)
print("INverse of a Matrix A :")
print(inverse)