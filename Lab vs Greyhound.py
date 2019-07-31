import numpy as np
import matplotlib.pyplot as plt
grey = 500
lab = 500
grey_height = 28 + 5*np.random.randn(grey)
lab_height = 24 + 5*np.random.randn(lab)
plt.hist([grey_height, lab_height], stacked=True, color=['r', 'y'])
plt.show()

