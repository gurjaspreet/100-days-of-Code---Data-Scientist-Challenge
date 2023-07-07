import numpy as np


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

print(f'A: {np.any(A, axis = 0)}')
print(f'B: {np.any(B, axis = 0)}')
print(f'C: {np.any(C, axis = 0)}')
print(f'D: {np.any(D, axis = 0)}')