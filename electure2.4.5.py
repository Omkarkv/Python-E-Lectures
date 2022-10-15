import numpy as np
import numpy.random as rnd

rnd.seed(10)

first = rnd.randn(10000, 1)

answer = len(first[(first < 2) & (first > -2)]) / 10000

# print(answer)