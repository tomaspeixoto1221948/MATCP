# 2x4 dimension matrix
import numpy as np
x = np.array([[1, 2, 5, 9], [3, 4, 6, 8]])
print(f"{x.ndim}, {x.shape}, {x.dtype}")

# Set data type
y = np.array([[1, 2], [3, 4]], float)
print(x[0][1])

# Redistribute elements by a given number of rows and columns
z = np.array([1, 2, 3, 4, 5, 6])
print(f"beginning z: {z}")
zreshape = z.reshape(2, 3)
print(f"reshaped z: {zreshape}")

A = np.array(np.arange(16).reshape(4, 4))
print(A)
print(A[1, 2])
print(A[[1, 3]])
print(A[:, [0, 2]])
print(A[[0, 2], :])
print(A[[1, 3]][:, [0, 2]])
print(A[[1, 3], [0, 2]])