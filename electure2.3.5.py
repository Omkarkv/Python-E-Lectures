import numpy as np
import numpy.random as rnd
import scipy.linalg as la


rnd.seed(4)

first = rnd.rand(5, 5)

t = la.toeplitz(np.arange(1, 6))

answer = np.sum(np.vstack((np.transpose(first), np.transpose(t)))[:, 0])
print(answer)

