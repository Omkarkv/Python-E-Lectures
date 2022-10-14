import numpy as np

Imatrix = np.identity(25)

answer = sum([Imatrix[val, val] for val in range(0, 25)])

answer2 = np.trace(np.eye(25))