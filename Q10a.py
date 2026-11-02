import numpy as np

#  Define Matrix A
A = np.array([[1,2],
              [5,1]
    ])

#  Define Matrix B
B = np.array([[7,2],
              [0,3]
    ])

#display 
print("\nMatrix A")
print(A)
#display 
print("\nMatrix B")
print(B)

# Addition of Matrix
print("\nMatrix A + B ")
print(A+B)

# Subtraction of Matrix
print("\nMatrix A - B ")
print(A-B)

# MUltiplication of Matrix
print("\nMatrix A x B ")
print(np.multiply(A,B))

# Transpose of A 
print("\nTranspose of A")
print(A.T)

# Transpose of B
print("\nTranspose of B")
print(B.T)