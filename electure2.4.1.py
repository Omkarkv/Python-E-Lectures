import numpy as np
import numpy.random as rnd
import scipy.linalg as la

rnd.seed(2)

first = rnd.randn(5, 5)

eigens = la.eigvals(first)

min_abs = float('inf')
max_abs = float('-inf')
min_answer = None
max_answer = None

for val in eigens:

    if np.abs(val) < min_abs:
        min_answer = np.real(val)
        min_abs = np.abs(val)

    if np.abs(val) > max_abs:
        max_answer = np.real(val)
        max_abs = np.abs(val)

# print(eigens)
# print(min_answer, max_answer)
# print([np.abs(val) for val in eigens])