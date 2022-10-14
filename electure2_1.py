import numpy.random as rnd

rnd.seed(5)  # reset the random number generator
print('random number ', rnd.rand())  # get a single number out

xr = rnd.get_state()
print(xr)