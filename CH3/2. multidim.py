import numpy as np

# A = np.array([[1,2,3],[4,5,6]])
A = np.array([[1,2],[5,6]])
print(A.shape)

# B = np.array([[1,2],[3,4],[5,6]])
B = np.array([1,2])
print(B.shape)
print(np.dot(A, B).shape)
print(np.dot(A, B))
