import numpy as np

answer = np.sum(np.reshape(np.sin(np.arange(0, 5.1, 0.1)), -1))
print(answer)