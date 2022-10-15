import numpy as np


dd  = 4 + -4j
ee = -2 + -3j
ff = 4 + -3j
print(np.angle(dd, deg=True), np.angle(ee, deg=True), np.angle(ff, deg=True))
print(np.abs(dd), np.abs(ee), np.abs(ff))