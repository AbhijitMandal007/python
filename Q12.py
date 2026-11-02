import numpy as np

#  Define Matrix A
A = np.array([[1,2],
              [5,1]
    ])
# eiganvalue & eiganvector

eiganvalue , eiganvector = np.linalg.eig(A)
print("eiganvalue = ",eiganvalue)
print("eiganvector = " ,eiganvector)
