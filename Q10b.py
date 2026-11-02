# Without Using Numpy

# Define Matrix A
A = [[8,5],
     [1,3]]

# Define Matrix B
B = [[1,5],
     [4,5]] 

# Display A
print("\nMatrix A ")
for row in A:
    print(row)

# Display B
print("\nMatrix B")
for row in B:
    print(row)  

 # ADDITION
add =[]
for i in range(len(A)):
    row = []
    for j in range(len(B)):
        row.append(A[i][j] + B[i][j]) 
    add.append(row)
print("\nMatrix A + B ")
for row in add:
    print(row)            

# SUBTRACTION
sub =[]
for i in range(len(A)):
    row = []
    for j in range(len(B)):
        row.append(A[i][j] - B[i][j]) 
    add.append(row)
print("\nMatrix A - B ")
for row in sub:
    print(row)



# TARNSPOSE OF A
A_trans  = [ ]
for i  in range(len(A)):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    A_trans.append(row)

print("Transpose of A ")
for row in A_trans:
    print(row)

# TARNSPOSE OF B
B_trans  = [ ]
for i  in range(len(B)):
    row = []
    for j in range(len(B)):
        row.append(A[j][i])
    B_trans.append(row)

print("Transpose of B ")
for row in B_trans:
    print(row)        
print("hello")