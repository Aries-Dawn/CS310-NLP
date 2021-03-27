import numpy as np

A = np.random.randint(0, 10, size=[5, 4])
B = np.random.randint(0, 10, size=[5, 4])
# print(A, B)
temp = np.copy(A[0])
A[0] = B[0]
B[0] = temp
# print(A, B)
C = np.concatenate((A, B), axis=0)
print(C.shape)
print(C.max())
print(C.min())
print(C.mean())
print(C.sum())
