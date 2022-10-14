import numpy.random as rnd
import numpy as np

rnd.seed(3)

first = rnd.rand(6, 6)

first[4, :] = [x for x in range(2, 8)]

sum_first = np.sum(first)
print(sum_first)
