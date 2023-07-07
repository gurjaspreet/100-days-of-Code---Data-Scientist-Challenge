import numpy as np


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

print(f'A: {np.any(A)}')
print(f'B: {np.any(B)}')
print(f'C: {np.any(C)}')
print(f'D: {np.any(D)}')