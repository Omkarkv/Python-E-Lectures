import numpy as np
import numpy.random as rnd

rnd.seed(9)

first = rnd.randn(20, 70)

answer = np.sum(first[first >= 2])
# print(answer)