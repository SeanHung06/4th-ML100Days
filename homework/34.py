import numpy as np
X = np.arange(1000).reshape(200, 5)
y = np.zeros(200)
y[:40] = 1

from sklearn.model_selection import train_test_split
y_1_index,y_0_index = np.where