import numpy.random as rnd
import numpy as np

rnd.seed(9)

first = np.round(rnd.randn(5, 5))

rowvector = np.arange(-2,3).reshape((1,5))
columnvector = np.arange(0,6).reshape((6, 1))

first = np.hstack((np.vstack((first, rowvector)), columnvector))

print(np.count_nonzero(first))