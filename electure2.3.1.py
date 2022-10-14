import numpy.random as rnd
import numpy as np


rnd.seed(6)

matrix = rnd.rand(15, 7)

print(np.sum(matrix[:, 5]))

