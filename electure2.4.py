import numpy as np
import numpy.random as rnd
keepthis = np.sin(0.4)           # scalar variable
a = np.sin([1, 2, 3])     # python array of 3 elements
a = np.sin(np.matrix([[1.0, 3.0],[0.0, 5.0]])) # with a numpy matrix
# making some matrices to play with
a = np.matrix('1.0; 2.0; 3.0; 4.0')
b = rnd.rand(4, 5)
c = np.arange(1,7)


# when you are creating test input signals, ones and zeros are useful
d = np.zeros((100,1))
e = np.ones((20,1))


# note that the c matrix ends at value 6, typically, 
# python ranges don't include the end value

# the hstack function takes a sequence of matrices
f = np.hstack((b, a))


# the vstack does the same. 
r = np.vstack( (np.hstack( (b, a,) ), c,) )

# also note that the c matrix was implicitly converted from
# integer to double

a = np.matrix('1 2 3; 4 5 6')
print(a)
# print(a[np.matrix([[True, True, True], [False, False, True]])])
print(a[np.matrix([[True, False, False], [False, False, True]])])
print(a[a >= 2])