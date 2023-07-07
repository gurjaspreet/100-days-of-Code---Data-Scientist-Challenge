import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])
              
print(f'A: {np.all(A, axis = 1)}')
print(f'B: {np.all(B, axis = 1)}')
print(f'C: {np.all(C, axis = 1)}')