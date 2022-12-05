from sympy import Matrix
from sympy.matrices import dense

A = Matrix([[1,2,1,1],
            [2,1,-2,-2],
            [1,-1,-4,3]])
A_rref = A.rref()
print(A_rref)
B = Matrix([[1,1,1],
            [0,0,0],
            [0,0,0]])
B_rref = B.rref()
print(B_rref)
