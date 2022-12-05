import numpy as np
# from  numpy import a
a = np.ones((4,4))
b = np.eye(4)
print(a)
print(b)
# b.reversed()
A = np.array([[1,3],
              [3,4]])
print(A)
B = A
print(A*A)
print(np.dot(A,A))
det_A=np.linalg.det(A)
print(np.linalg.det(A))
A = np.matrix(A)
inv_A=np.linalg.inv(A)
# print(inv_A)
print(det_A*inv_A)
